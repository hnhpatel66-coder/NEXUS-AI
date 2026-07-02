from PySide6.QtWidgets import (
    QMainWindow,
    QLabel
)
from PySide6.QtCore import Qt


class DashboardWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("NEXUS AI Dashboard")
        self.resize(1200, 700)

        label = QLabel("🎉 Welcome to NEXUS AI Dashboard")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)