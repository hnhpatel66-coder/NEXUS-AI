from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt


class SettingsPage(QWidget):

    def __init__(self):
        super().__init__()

        self.setStyleSheet("background:#111827;")

        layout = QVBoxLayout()

        title = QLabel("⚙️ Settings")
        title.setAlignment(Qt.AlignCenter)

        title.setStyleSheet("""
            color:white;
            font-size:30px;
            font-weight:bold;
        """)

        layout.addStretch()
        layout.addWidget(title)
        layout.addStretch()

        self.setLayout(layout)