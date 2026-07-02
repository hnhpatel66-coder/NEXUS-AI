from ui.login.login_window import LoginWindow

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QProgressBar,
)
from PySide6.QtCore import Qt, QTimer


class SplashScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("NEXUS AI")
        self.setFixedSize(700, 400)

        self.setStyleSheet("""
            QWidget{
                background-color:#111827;
                color:white;
                font-family:Segoe UI;
            }

            QLabel{
                font-size:28px;
                font-weight:bold;
            }

            QProgressBar{
                border:2px solid #2563EB;
                border-radius:10px;
                text-align:center;
                height:20px;
            }

            QProgressBar::chunk{
                background:#2563EB;
                border-radius:8px;
            }
        """)

        layout = QVBoxLayout()

        layout.addStretch()

        title = QLabel("🚀 NEXUS AI")
        title.setAlignment(Qt.AlignCenter)

        subtitle = QLabel("Building Future with Artificial Intelligence")
        subtitle.setAlignment(Qt.AlignCenter)

        self.progress = QProgressBar()
        self.progress.setValue(0)

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addSpacing(25)
        layout.addWidget(self.progress)

        layout.addStretch()

        self.setLayout(layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(30)

    def update_progress(self):
        value = self.progress.value()

        if value < 100:
            self.progress.setValue(value + 1)
        else:
            self.timer.stop()

            # Login Window Open
            self.login_window = LoginWindow()
            self.login_window.show()

            # Splash Close
            self.close()