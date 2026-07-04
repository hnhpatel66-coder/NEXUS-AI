from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
    QMessageBox,
    QSizePolicy,
)

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

from auth.auth_service import AuthService


class RegisterWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("NEXUS AI - Register")
        self.setFixedSize(1300, 750)

        self.setStyleSheet("""

        QWidget{
            background:#0F172A;
            color:white;
            font-family:'Segoe UI';
        }

        #card{
            background:#1E293B;
            border-radius:20px;
            border:1px solid #334155;
        }

        QLabel{
            background:transparent;
        }

        QLineEdit{
            background:#111827;
            border:2px solid #334155;
            border-radius:12px;
            padding:14px;
            font-size:15px;
        }

        QLineEdit:focus{
            border:2px solid #3B82F6;
        }

        QPushButton{
            background:#2563EB;
            color:white;
            border:none;
            border-radius:12px;
            padding:14px;
            font-size:15px;
            font-weight:bold;
        }

        QPushButton:hover{
            background:#3B82F6;
        }

        """)

        root = QHBoxLayout(self)
        root.setContentsMargins(70,50,70,50)
        root.setSpacing(60)

        # ===============================
        # LEFT PANEL
        # ===============================

        left = QVBoxLayout()

        left.setAlignment(Qt.AlignCenter)

        logo = QLabel("🤖")
        logo.setFont(QFont("Segoe UI Emoji",80))
        logo.setAlignment(Qt.AlignCenter)

        title = QLabel("Create Account")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            font-size:42px;
            font-weight:800;
            color:#60A5FA;
        """)

        subtitle = QLabel(
            "Join NEXUS AI Today"
        )

        subtitle.setAlignment(Qt.AlignCenter)

        subtitle.setStyleSheet("""
            font-size:18px;
            color:#94A3B8;
        """)

        desc = QLabel(
            "Start Building\n"
            "Future With AI"
        )

      
      
        desc.setAlignment(Qt.AlignCenter)

        desc.setStyleSheet("""
            font-size:15px;
            color:#CBD5E1;
            line-height:24px;
        """)

        left.addStretch()
        left.addWidget(logo)
        left.addWidget(title)
        left.addSpacing(10)
        left.addWidget(subtitle)
        left.addSpacing(25)
        left.addWidget(desc)
        left.addStretch()
                # ===============================
        # RIGHT PANEL
        # ===============================

        card = QFrame()
        card.setObjectName("card")
        card.setFixedWidth(470)

        card_layout = QVBoxLayout(card)

        card_layout.setContentsMargins(
            40,
            40,
            40,
            40
        )

        card_layout.setSpacing(18)

        # ===============================
        # TITLE
        # ===============================

        register_title = QLabel("Register")

        register_title.setAlignment(Qt.AlignCenter)

        register_title.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
        """)

        register_subtitle = QLabel(
            "Create your NEXUS AI account"
        )

        register_subtitle.setAlignment(Qt.AlignCenter)

        register_subtitle.setStyleSheet("""
            font-size:14px;
            color:#94A3B8;
        """)

        # ===============================
        # FULL NAME
        # ===============================

        name_label = QLabel("Full Name")

        name_label.setStyleSheet("""
            font-size:14px;
            font-weight:bold;
        """)

        self.name = QLineEdit()

        self.name.setPlaceholderText(
            "Enter your full name"
        )

        # ===============================
        # EMAIL
        # ===============================

        email_label = QLabel("Email")

        email_label.setStyleSheet("""
            font-size:14px;
            font-weight:bold;
        """)

        self.email = QLineEdit()

        self.email.setPlaceholderText(
            "Enter your email"
        )

        # ===============================
        # PASSWORD
        # ===============================

        password_label = QLabel("Password")

        password_label.setStyleSheet("""
            font-size:14px;
            font-weight:bold;
        """)

        self.password = QLineEdit()

        self.password.setPlaceholderText(
            "Create password"
        )

        self.password.setEchoMode(
            QLineEdit.Password
        )

        # ===============================
        # CONFIRM PASSWORD
        # ===============================

        confirm_label = QLabel("Confirm Password")

        confirm_label.setStyleSheet("""
            font-size:14px;
            font-weight:bold;
        """)

        self.confirm_password = QLineEdit()

        self.confirm_password.setPlaceholderText(
            "Confirm password"
        )

        self.confirm_password.setEchoMode(
            QLineEdit.Password
        )

        # ===============================
        # BUTTONS
        # ===============================

        self.register_btn = QPushButton(
            "Create Account"
        )

        self.login_btn = QPushButton(
            "Already have an account?"
        )

        self.login_btn.setStyleSheet("""

        QPushButton{

            background:#334155;

            color:white;

            border:none;

            border-radius:12px;

            padding:14px;

            font-size:15px;

            font-weight:bold;

        }

        QPushButton:hover{

            background:#475569;

        }

        """)

        # ===============================
        # ADD WIDGETS
        # ===============================

        card_layout.addWidget(register_title)
        card_layout.addWidget(register_subtitle)

        card_layout.addSpacing(15)

        card_layout.addWidget(name_label)
        card_layout.addWidget(self.name)

        card_layout.addWidget(email_label)
        card_layout.addWidget(self.email)

        card_layout.addWidget(password_label)
        card_layout.addWidget(self.password)

        card_layout.addWidget(confirm_label)
        card_layout.addWidget(self.confirm_password)

        card_layout.addSpacing(10)

        card_layout.addWidget(self.register_btn)
        card_layout.addWidget(self.login_btn)

        root.addLayout(left, 1)
        root.addWidget(card)
                # ===============================
        # EVENTS
        # ===============================

        self.register_btn.clicked.connect(
            self.register
        )

        self.login_btn.clicked.connect(
            self.open_login
        )

        self.confirm_password.returnPressed.connect(
            self.register
        )

    # =====================================
    # REGISTER
    # =====================================

    def register(self):

        username = self.name.text().strip()
        email = self.email.text().strip()
        password = self.password.text()
        confirm = self.confirm_password.text()

        # -----------------------------
        # Validation
        # -----------------------------

        if username == "":
            QMessageBox.warning(
                self,
                "Validation",
                "Please enter your full name."
            )
            return

        if email == "":
            QMessageBox.warning(
                self,
                "Validation",
                "Please enter your email."
            )
            return

        if "@" not in email or "." not in email:
            QMessageBox.warning(
                self,
                "Validation",
                "Invalid email address."
            )
            return

        if password == "":
            QMessageBox.warning(
                self,
                "Validation",
                "Please enter password."
            )
            return

        if len(password) < 6:
            QMessageBox.warning(
                self,
                "Validation",
                "Password must contain at least 6 characters."
            )
            return

        if password != confirm:
            QMessageBox.warning(
                self,
                "Validation",
                "Passwords do not match."
            )
            return

        # -----------------------------
        # Register User
        # -----------------------------

        success, message = AuthService.register_user(
            username,
            email,
            password
        )

        if success:

            QMessageBox.information(
                self,
                "Success",
                message
            )

            self.open_login()

        else:

            QMessageBox.warning(
                self,
                "Registration Failed",
                message
            )

    # =====================================
    # OPEN LOGIN
    # =====================================

    def open_login(self):

        from ui.login.login_window import LoginWindow

        self.login = LoginWindow()

        self.login.show()

        self.close()