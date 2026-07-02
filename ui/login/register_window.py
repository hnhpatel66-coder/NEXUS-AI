from auth.auth_service import AuthService

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QMessageBox
)

from PySide6.QtCore import Qt


class RegisterWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("NEXUS AI - Register")
        self.resize(450, 600)

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

        title = QLabel("Create Account")
        title.setAlignment(Qt.AlignCenter)

        self.full_name = QLineEdit()
        self.full_name.setPlaceholderText("Full Name")

        self.email = QLineEdit()
        self.email.setPlaceholderText("Email Address")

        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)

        self.confirm_password = QLineEdit()
        self.confirm_password.setPlaceholderText("Confirm Password")
        self.confirm_password.setEchoMode(QLineEdit.Password)

        self.register_btn = QPushButton("Register")

        layout.addWidget(title)
        layout.addSpacing(20)
        layout.addWidget(self.full_name)
        layout.addWidget(self.email)
        layout.addWidget(self.password)
        layout.addWidget(self.confirm_password)
        layout.addSpacing(10)
        layout.addWidget(self.register_btn)

        self.setLayout(layout)

        self.register_btn.clicked.connect(self.register)

    def register(self):

        full_name = self.full_name.text().strip()
        email = self.email.text().strip()
        password = self.password.text()
        confirm_password = self.confirm_password.text()

        if not full_name or not email or not password or not confirm_password:
            QMessageBox.warning(
                self,
                "Error",
                "Please fill all fields."
            )
            return

        if password != confirm_password:
            QMessageBox.warning(
                self,
                "Error",
                "Passwords do not match."
            )
            return

        success, message = AuthService.register_user(
            full_name,
            email,
            password
        )

        if success:
            QMessageBox.information(
                self,
                "Success",
                message
            )

            self.full_name.clear()
            self.email.clear()
            self.password.clear()
            self.confirm_password.clear()

        else:
            QMessageBox.warning(
                self,
                "Error",
                message
            )