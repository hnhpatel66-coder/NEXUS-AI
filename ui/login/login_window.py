from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QCheckBox,
    QMessageBox
)
from PySide6.QtCore import Qt

from auth.auth_service import AuthService
from ui.login.register_window import RegisterWindow
from ui.dashboard.dashboard_window import DashboardWindow


class LoginWindow(QWidget):

    def __init__(self):
        super().__init__()

        print("LOGIN WINDOW LOADED")
        self.setWindowTitle("NEXUS AI - Login")
        self.resize(450, 520)

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

        self.email = QLineEdit()
        self.email.setPlaceholderText("Email")

        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)

        remember = QCheckBox("Remember Me")

        self.login_btn = QPushButton("Login")
        self.register_btn = QPushButton("Create New Account")

        layout.addWidget(title)
        layout.addSpacing(20)
        layout.addWidget(self.email)
        layout.addWidget(self.password)
        layout.addWidget(remember)
        layout.addSpacing(10)
        layout.addWidget(self.login_btn)
        layout.addWidget(self.register_btn)

        self.setLayout(layout)

        self.login_btn.clicked.connect(self.login)
        self.register_btn.clicked.connect(self.open_register)

    def login(self):

        QMessageBox.information(self, "Test", "Login Button Clicked")
        
        print("LOGIN BUTTON CLICKED")
        email = self.email.text().strip()
        password = self.password.text()

        if not email or not password:
            QMessageBox.warning(
                self,
                "Error",
                "Please enter Email and Password."
            )
            return

        success = AuthService.login_user(email, password)

        if success:
            QMessageBox.information(
                self,
                "Success",
                "Login Successful."
            )

            self.dashboard = DashboardWindow()
            self.dashboard.show()

            self.close()

        else:
            QMessageBox.warning(
                self,
                "Error",
                "Invalid Email or Password."
            )

    def open_register(self):

        self.register = RegisterWindow()
        self.register.show()