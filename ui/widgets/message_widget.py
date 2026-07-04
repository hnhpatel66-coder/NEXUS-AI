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
    QTimer,
)

from PySide6.QtGui import (
    QGuiApplication,
)


class MessageWidget(QWidget):

    # Regenerate Signal
    regenerate_requested = Signal(str)

    def __init__(self, sender, message):

        super().__init__()

        self.sender = sender
        self.message = message

        # =====================================
        # MAIN LAYOUT
        # =====================================

        self.main_layout = QHBoxLayout(self)

        self.main_layout.setContentsMargins(
            10,
            8,
            10,
            8
        )

        self.main_layout.setSpacing(10)

        # =====================================
        # MESSAGE CARD
        # =====================================

        self.card = QFrame()

        self.card.setMaximumWidth(900)

        # =====================================
        # USER STYLE
        # =====================================

        if sender == "user":

            self.card.setStyleSheet("""

            QFrame{

                background:#2563EB;

                border-radius:18px;

            }

            """)

            self.main_layout.addStretch()

            self.main_layout.addWidget(
                self.card
            )

        # =====================================
        # AI STYLE
        # =====================================

        else:

            self.card.setStyleSheet("""

            QFrame{

                background:#1E293B;

                border:1px solid #334155;

                border-radius:18px;

            }

            """)

            self.main_layout.addWidget(
                self.card
            )

            self.main_layout.addStretch()

        # =====================================
        # CARD LAYOUT
        # =====================================

        self.card_layout = QVBoxLayout(
            self.card
        )

        self.card_layout.setContentsMargins(
            16,
            14,
            16,
            14
        )

        self.card_layout.setSpacing(10)
                # =====================================
        # HEADER
        # =====================================

        header = QHBoxLayout()

        self.title = QLabel(
            "You" if self.sender == "user" else "🤖 NEXUS AI"
        )

        self.title.setStyleSheet("""

        color:#94A3B8;

        font-size:12px;

        font-weight:bold;

        """)

        header.addWidget(self.title)

        header.addStretch()

        # =====================================
        # COPY BUTTON
        # =====================================

        self.copy_btn = QPushButton("📋")

        self.copy_btn.setCursor(
            Qt.PointingHandCursor
        )

        self.copy_btn.setFixedSize(34,34)

        self.copy_btn.setStyleSheet("""

        QPushButton{

            background:transparent;

            border:none;

            color:#94A3B8;

            font-size:15px;

        }

        QPushButton:hover{

            color:white;

            background:#334155;

            border-radius:8px;

        }

        """)

        self.copy_btn.clicked.connect(
            self.copy_message
        )

        header.addWidget(self.copy_btn)

        # =====================================
        # MESSAGE BODY
        # =====================================

        self.body = QLabel()

        self.body.setWordWrap(True)

        self.body.setText(message)

        self.body.setTextInteractionFlags(
            Qt.TextSelectableByMouse
        )

        self.body.setStyleSheet("""

        color:white;

        font-size:14px;

        padding-top:4px;

        line-height:22px;

        """)

        # =====================================
        # ADD TO CARD
        # =====================================

        self.card_layout.addLayout(header)

        self.card_layout.addWidget(
            self.body
        )
                # =====================================
        # TOOLBAR
        # =====================================

        toolbar = QHBoxLayout()
        toolbar.setSpacing(6)

        toolbar.addStretch()

        # ---------- COPY ----------
        toolbar.addWidget(self.copy_btn)

        # ---------- AI ONLY ----------
        if self.sender == "ai":

            button_style = """
            QPushButton{
                background:transparent;
                border:none;
                color:#94A3B8;
                font-size:15px;
                border-radius:8px;
                padding:4px;
            }

            QPushButton:hover{
                background:#334155;
                color:white;
            }
            """

            # 👍 Like
            self.like_btn = QPushButton("👍")
            self.like_btn.setFixedSize(34,34)
            self.like_btn.setStyleSheet(button_style)
            self.like_btn.clicked.connect(
                lambda: self.like_btn.setText("❤️")
            )

            toolbar.addWidget(self.like_btn)

            # 👎 Dislike
            self.dislike_btn = QPushButton("👎")
            self.dislike_btn.setFixedSize(34,34)
            self.dislike_btn.setStyleSheet(button_style)
            self.dislike_btn.clicked.connect(
                lambda: self.dislike_btn.setText("❌")
            )

            toolbar.addWidget(self.dislike_btn)

            # 💾 Download
            self.download_btn = QPushButton("💾")
            self.download_btn.setFixedSize(34,34)
            self.download_btn.setStyleSheet(button_style)
            self.download_btn.clicked.connect(
                self.download_message
            )

            toolbar.addWidget(self.download_btn)

            # 🔄 Regenerate
            self.regenerate_btn = QPushButton("🔄")
            self.regenerate_btn.setFixedSize(34,34)
            self.regenerate_btn.setStyleSheet(button_style)
            self.regenerate_btn.clicked.connect(
                self.regenerate
            )

            toolbar.addWidget(self.regenerate_btn)

        # =====================================
        # ADD TOOLBAR
        # =====================================

        self.card_layout.addLayout(toolbar)
        