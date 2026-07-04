from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QFrame,
    QFileDialog,
)

from PySide6.QtCore import (
    Qt,
    Signal,
)

from PySide6.QtGui import (
    QGuiApplication,
    QTextDocument,
)


class MessageWidget(QWidget):

    regenerate_requested = Signal(str)

    def __init__(self, sender, message):

        super().__init__()

        self.sender = sender
        self.message = message

        self.main_layout = QHBoxLayout(self)

        self.main_layout.setContentsMargins(
            10,
            8,
            10,
            8
        )

        self.card = QFrame()

        self.card.setMaximumWidth(900)

        if sender == "user":

            self.main_layout.addStretch()

            self.main_layout.addWidget(self.card)

            self.card.setStyleSheet("""
            QFrame{
                background:#2563EB;
                border-radius:18px;
            }
            """)

        else:

            self.main_layout.addWidget(self.card)

            self.main_layout.addStretch()

            self.card.setStyleSheet("""
            QFrame{
                background:#1E293B;
                border:1px solid #334155;
                border-radius:18px;
            }
            """)

        self.card_layout = QVBoxLayout(self.card)

        self.card_layout.setContentsMargins(
            18,
            16,
            18,
            16
        )

        self.card_layout.setSpacing(10)

        # ===========================
        # Header
        # ===========================

        header = QHBoxLayout()

        self.title = QLabel(
            "You" if sender == "user" else "🤖 NEXUS AI"
        )

        self.title.setStyleSheet("""
            color:#94A3B8;
            font-size:12px;
            font-weight:bold;
        """)

        header.addWidget(self.title)

        header.addStretch()

        self.card_layout.addLayout(header)

        # ===========================
        # Message Body
        # ===========================

        self.body = QLabel()

        self.body.setWordWrap(True)

        self.body.setTextInteractionFlags(
            Qt.TextSelectableByMouse
        )

        self.body.setOpenExternalLinks(True)

        self.body.setStyleSheet("""
            color:white;
            font-size:14px;
            line-height:22px;
        """)

        self.body.setText(message)

        self.card_layout.addWidget(self.body)
                # =====================================
        # TOOLBAR
        # =====================================

        toolbar = QHBoxLayout()

        toolbar.setSpacing(6)

        toolbar.addStretch()

        button_style = """
        QPushButton{

            background:transparent;

            border:none;

            color:#94A3B8;

            font-size:15px;

            border-radius:8px;

            padding:5px;

        }

        QPushButton:hover{

            background:#334155;

            color:white;

        }
        """

        # =====================================
        # COPY
        # =====================================

        self.copy_btn = QPushButton("📋")

        self.copy_btn.setFixedSize(34, 34)

        self.copy_btn.setStyleSheet(button_style)

        self.copy_btn.clicked.connect(
            self.copy_message
        )

        toolbar.addWidget(self.copy_btn)

        # =====================================
        # AI TOOLS
        # =====================================

        if self.sender == "ai":

            # 👍 Like
            self.like_btn = QPushButton("👍")

            self.like_btn.setFixedSize(34, 34)

            self.like_btn.setStyleSheet(button_style)

            self.like_btn.clicked.connect(
                lambda: self.like_btn.setText("❤️")
            )

            toolbar.addWidget(self.like_btn)

            # 👎 Dislike
            self.dislike_btn = QPushButton("👎")

            self.dislike_btn.setFixedSize(34, 34)

            self.dislike_btn.setStyleSheet(button_style)

            self.dislike_btn.clicked.connect(
                lambda: self.dislike_btn.setText("❌")
            )

            toolbar.addWidget(self.dislike_btn)

            # 💾 Download
            self.download_btn = QPushButton("💾")

            self.download_btn.setFixedSize(34, 34)

            self.download_btn.setStyleSheet(button_style)

            self.download_btn.clicked.connect(
                self.download_message
            )

            toolbar.addWidget(self.download_btn)

            # 🔄 Regenerate
            self.regenerate_btn = QPushButton("🔄")

            self.regenerate_btn.setFixedSize(34, 34)

            self.regenerate_btn.setStyleSheet(button_style)

            self.regenerate_btn.clicked.connect(
                lambda: self.regenerate_requested.emit(
                    self.message
                )
            )

            toolbar.addWidget(
                self.regenerate_btn
            )

        self.card_layout.addLayout(toolbar)
            # =====================================
    # UPDATE MESSAGE (Streaming Support)
    # =====================================

    def set_message(self, text):

        self.message = text

        # HTML / Markdown rendered text
        self.body.setText(text)

    # =====================================
    # COPY MESSAGE
    # =====================================

    def copy_message(self):

        clipboard = QGuiApplication.clipboard()

        # Copy plain text only
        doc = QTextDocument()
        doc.setHtml(self.message)

        clipboard.setText(doc.toPlainText())

        self.copy_btn.setText("✅")

        from PySide6.QtCore import QTimer

        QTimer.singleShot(
            1200,
            lambda: self.copy_btn.setText("📋")
        )

    # =====================================
    # DOWNLOAD MESSAGE
    # =====================================

    def download_message(self):

        path, _ = QFileDialog.getSaveFileName(

            self,

            "Save AI Response",

            "response.txt",

            "Text File (*.txt);;Markdown (*.md);;HTML (*.html)"

        )

        if not path:
            return

        try:

            with open(
                path,
                "w",
                encoding="utf-8"
            ) as file:

                doc = QTextDocument()
                doc.setHtml(self.message)

                file.write(
                    doc.toPlainText()
                )

        except Exception as e:

            print("Download Error:", e)

    # =====================================
    # GET MESSAGE
    # =====================================

    def get_message(self):

        return self.message

    # =====================================
    # CLEAR MESSAGE
    # =====================================

    def clear_message(self):

        self.message = ""

        self.body.clear()

    # =====================================
    # APPEND STREAM TEXT
    # =====================================

    def append_text(self, text):

        self.message += text

        self.body.setText(self.message)

    # =====================================
    # SET HTML DIRECTLY
    # =====================================

    def set_html(self, html):

        self.message = html

        self.body.setText(html)