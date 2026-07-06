from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QFrame,
    QFileDialog,
    QApplication,
)

from PySide6.QtCore import (
    Qt,
    Signal,
    QTimer,
)

from PySide6.QtGui import (
    QCursor,
    QGuiApplication,
    QTextDocument,
)


class MessageWidget(QWidget):

    regenerate_requested = Signal(str)

    def __init__(self, sender: str, message: str = ""):

        super().__init__()

        self.sender = sender.lower()

        self.message = message

        # =========================================
        # MAIN LAYOUT
        # =========================================

        self.main_layout = QHBoxLayout(self)

        self.main_layout.setContentsMargins(
            10,
            8,
            10,
            8
        )

        self.main_layout.setSpacing(0)

        # =========================================
        # CARD
        # =========================================

        self.card = QFrame()

        self.card.setMaximumWidth(900)

        self.card_layout = QVBoxLayout(self.card)

        self.card_layout.setContentsMargins(
            18,
            16,
            18,
            16
        )

        self.card_layout.setSpacing(12)

        # =========================================
        # USER / AI POSITION
        # =========================================

        if self.sender == "user":

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

        # =========================================
        # HEADER
        # =========================================

        header = QHBoxLayout()

        self.title = QLabel(
            "You" if self.sender == "user"
            else "🤖 NEXUS AI"
        )

        self.title.setStyleSheet("""

        color:#94A3B8;

        font-size:12px;

        font-weight:bold;

        """)

        header.addWidget(self.title)

        header.addStretch()

        self.card_layout.addLayout(header)

        # =========================================
        # MESSAGE BODY
        # =========================================

        self.body = QLabel()

        self.body.setWordWrap(True)

        self.body.setTextInteractionFlags(
            Qt.TextSelectableByMouse |
            Qt.LinksAccessibleByMouse
        )

        self.body.setOpenExternalLinks(True)

        self.body.setStyleSheet("""

        QLabel{

            color:white;

            font-size:14px;

            line-height:22px;

            background:transparent;

        }

        """)

        self.body.setText(message)

        self.card_layout.addWidget(self.body)
        