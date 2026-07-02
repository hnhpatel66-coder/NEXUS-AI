from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QCheckBox
)
from PySide6.QtCore import Qt


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("NEXUS AI - Login")
        self.resize(450, 500)

        self.setStyleSheet("""
            QWidget{
                background:#111827;
                color:white;
                font-family:Segoe UI;
            }

            QLabel{
                font-size:22px;
                font-weight:bold;
            }

            QLineEdit{
                padding:10px;
                border:2px solid #2563EB;
                border-radius:8px;
                font-size:14px;
            }

            QPushButton{
                background:#2563EB;
                color:white;
                padding:10px;
                border-radius:8px;
                font-size:15px;
                font-weight:bold;
            }

            QPushButton:hover{
                background:#1D4ED8;
            }
        """)

        layout = QVBoxLayout()

        layout.setAlignment(Qt.AlignCenter)

        title = QLabel("NEXUS AI Login")
        title.setAlignment(Qt.AlignCenter)

        email = QLineEdit()
        email.setPlaceholderText("Email")

        password = QLineEdit()
        password.setPlaceholderText("Password")
        password.setEchoMode(QLineEdit.Password)

        remember = QCheckBox("Remember Me")

        login = QPushButton("Login")

        layout.addWidget(title)
        layout.addSpacing(20)
        layout.addWidget(email)
        layout.addWidget(password)
        layout.addWidget(remember)
        layout.addSpacing(10)
        layout.addWidget(login)

        self.setLayout(layout)