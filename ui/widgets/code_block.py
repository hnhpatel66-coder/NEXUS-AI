from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QFrame
from PySide6.QtGui import QFont, QGuiApplication
from PySide6.QtCore import Qt


class CodeBlock(QWidget):

    def __init__(self, language, code):
        super().__init__()

        self.language = language
        self.code = code

        # =========================
        # MAIN CONTAINER
        # =========================
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(10, 8, 10, 8)

        # =========================
        # OUTER FRAME
        # =========================
        self.frame = QFrame()
        self.frame.setStyleSheet("""
            QFrame {
                background:#0B1220;
                border:1px solid #334155;
                border-radius:14px;
            }
        """)

        frame_layout = QVBoxLayout()
        frame_layout.setContentsMargins(12, 10, 12, 10)
        frame_layout.setSpacing(8)

        # =========================
        # HEADER BAR
        # =========================
        header = QHBoxLayout()

        lang_label = QLabel(language.upper())
        lang_label.setStyleSheet("""
            color:#60A5FA;
            font-weight:bold;
            font-size:12px;
        """)

        header.addWidget(lang_label)
        header.addStretch()

        # COPY BUTTON
        copy_btn = QPushButton("Copy")
        copy_btn.setCursor(Qt.PointingHandCursor)

        copy_btn.setStyleSheet("""
            QPushButton {
                background:#1E293B;
                color:white;
                border:none;
                padding:6px 12px;
                border-radius:8px;
                font-size:12px;
            }

            QPushButton:hover {
                background:#334155;
            }
        """)

        copy_btn.clicked.connect(self.copy_code)

        header.addWidget(copy_btn)

        # =========================
        # CODE LABEL
        # =========================
        self.code_label = QLabel()
        self.code_label.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.code_label.setFont(QFont("Consolas", 10))
        self.code_label.setStyleSheet("""
            color:#E5E7EB;
            background:transparent;
        """)

        self.code_label.setText(self.code)

        # =========================
        # ADD TO LAYOUT
        # =========================
        frame_layout.addLayout(header)
        frame_layout.addWidget(self.code_label)

        self.frame.setLayout(frame_layout)
        main_layout.addWidget(self.frame)

        self.setLayout(main_layout)

    # =========================
    # COPY FUNCTION
    # =========================
    def copy_code(self):

        clipboard = QGuiApplication.clipboard()
        clipboard.setText(self.code)

        # small feedback
        self.code_label.setText(self.code + "\n\n✅ Copied!")