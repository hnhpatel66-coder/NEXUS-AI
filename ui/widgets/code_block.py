from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
)

from PySide6.QtGui import (
    QFont,
    QGuiApplication,
)

from PySide6.QtCore import (
    Qt,
    QTimer,
)


class CodeBlock(QWidget):

    def __init__(self, language: str, code: str):

        super().__init__()

        self.language = language
        self.code = code

        # ==================================
        # MAIN LAYOUT
        # ==================================

        self.main_layout = QVBoxLayout(self)

        self.main_layout.setContentsMargins(
            10,
            8,
            10,
            8
        )

        self.main_layout.setSpacing(0)

        # ==================================
        # FRAME
        # ==================================

        self.frame = QFrame()

        self.frame.setStyleSheet("""

        QFrame{

            background:#0B1220;

            border:1px solid #334155;

            border-radius:14px;

        }

        """)

        self.frame_layout = QVBoxLayout(
            self.frame
        )

        self.frame_layout.setContentsMargins(
            0,
            0,
            0,
            0
        )

        self.frame_layout.setSpacing(0)
                # ==================================
        # HEADER
        # ==================================

        self.header = QWidget()

        self.header.setFixedHeight(42)

        self.header.setStyleSheet("""

        QWidget{

            background:#111827;

            border-top-left-radius:14px;

            border-top-right-radius:14px;

            border-bottom:1px solid #334155;

        }

        """)

        header_layout = QHBoxLayout(self.header)

        header_layout.setContentsMargins(
            14,
            6,
            14,
            6
        )

        # ==================================
        # LANGUAGE LABEL
        # ==================================

        self.language_label = QLabel(
            self.language.upper()
        )

        self.language_label.setStyleSheet("""

        color:#60A5FA;

        font-size:12px;

        font-weight:bold;

        """)

        header_layout.addWidget(
            self.language_label
        )

        header_layout.addStretch()

        # ==================================
        # COPY BUTTON
        # ==================================

        self.copy_btn = QPushButton("📋 Copy")

        self.copy_btn.setCursor(
            Qt.PointingHandCursor
        )

        self.copy_btn.setStyleSheet("""

        QPushButton{

            background:#1E293B;

            color:white;

            border:none;

            border-radius:8px;

            padding:6px 12px;

            font-size:12px;

            font-weight:bold;

        }

        QPushButton:hover{

            background:#334155;

        }

        """)

        self.copy_btn.clicked.connect(
            self.copy_code
        )

        header_layout.addWidget(
            self.copy_btn
        )

        self.frame_layout.addWidget(
            self.header
        )

        # ==================================
        # CODE LABEL
        # ==================================

        self.code_label = QLabel()

        self.code_label.setText(self.code)

        self.code_label.setTextInteractionFlags(
            Qt.TextSelectableByMouse
        )

        self.code_label.setFont(
            QFont("Consolas", 11)
        )

        self.code_label.setStyleSheet("""

        QLabel{

            background:#0B1220;

            color:#E5E7EB;

            padding:16px;

            border-bottom-left-radius:14px;

            border-bottom-right-radius:14px;

        }

        """)

        self.frame_layout.addWidget(
            self.code_label
        )

        self.main_layout.addWidget(
            self.frame
        )
        