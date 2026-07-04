from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
    QCheckBox,
    QMessageBox,
)

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

from auth.auth_service import AuthService
from ui.dashboard.dashboard_window import DashboardWindow
from ui.login.register_window import RegisterWindow


class LoginWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.dashboard = None

        self.setWindowTitle("NEXUS AI")
        self.setFixedSize(1300, 750)

        self.setStyleSheet("""

        QWidget{
            background:#0F172A;
            color:white;
            font-family:'Segoe UI';
        }

        #card{
            background:#1E293B;
            border-radius:22px;
            border:1px solid #334155;
        }

        QLabel{
            background:transparent;
            color:white;
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

        QCheckBox{
            font-size:14px;
        }

        """)

        root = QHBoxLayout(self)
        root.setContentsMargins(70,50,70,50)
        root.setSpacing(70)

        # ===========================
        # LEFT SIDE
        # ===========================

        left = QVBoxLayout()
        left.setAlignment(Qt.AlignCenter)

        logo = QLabel("🤖")
        logo.setAlignment(Qt.AlignCenter)
        logo.setFont(QFont("Segoe UI Emoji",80))

        title = QLabel("NEXUS AI")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            font-size:52px;
            font-weight:800;
            color:#60A5FA;
        """)

        subtitle = QLabel("Your Personal AI Assistant")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet("""
            font-size:18px;
            color:#94A3B8;
        """)

        description = QLabel(
            "Experience the next generation of\n"
            "Artificial Intelligence.\n\n"
            "Chat • Code • Create • Learn"
        )

        description.setAlignment(Qt.AlignCenter)

        description.setStyleSheet("""
            font-size:15px;
            color:#CBD5E1;
            line-height:24px;
        """)

        left.addStretch()
        left.addWidget(logo)
        left.addSpacing(15)
        left.addWidget(title)
        left.addSpacing(10)
        left.addWidget(subtitle)
        left.addSpacing(25)
        left.addWidget(description)
        left.addStretch()
                # ===========================
        # RIGHT SIDE (LOGIN CARD)
        # ===========================

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

        # --------------------------
        # TITLE
        # --------------------------

        login_title = QLabel("Welcome Back")

        login_title.setAlignment(Qt.AlignCenter)

        login_title.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
        """)

        login_subtitle = QLabel(
            "Login to continue"
        )

        login_subtitle.setAlignment(Qt.AlignCenter)

        login_subtitle.setStyleSheet("""
            font-size:14px;
            color:#94A3B8;
        """)

        # --------------------------
        # EMAIL
        # --------------------------

        email_label = QLabel("Email")

        email_label.setStyleSheet("""
            font-size:14px;
            font-weight:bold;
        """)

        self.email = QLineEdit()

        self.email.setPlaceholderText(
            "Enter your email"
        )

        # --------------------------
        # PASSWORD
        # --------------------------

        password_label = QLabel("Password")

        password_label.setStyleSheet("""
            font-size:14px;
            font-weight:bold;
        """)

        self.password = QLineEdit()

        self.password.setPlaceholderText(
            "Enter your password"
        )

        self.password.setEchoMode(
            QLineEdit.Password
        )

        # --------------------------
        # REMEMBER ME
        # --------------------------

        remember_layout = QHBoxLayout()

        self.remember = QCheckBox(
            "Remember Me"
        )

        remember_layout.addWidget(
            self.remember
        )

        remember_layout.addStretch()

        # --------------------------
        # BUTTONS
        # --------------------------

        self.login_btn = QPushButton(
            "Login"
        )

        self.register_btn = QPushButton(
            "Create New Account"
        )

        self.register_btn.setStyleSheet("""

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

        # --------------------------
        # ADD WIDGETS
        # --------------------------

        card_layout.addWidget(login_title)
        card_layout.addWidget(login_subtitle)

        card_layout.addSpacing(15)

        card_layout.addWidget(email_label)
        card_layout.addWidget(self.email)

        card_layout.addWidget(password_label)
        card_layout.addWidget(self.password)

        card_layout.addLayout(
            remember_layout
        )

        card_layout.addSpacing(10)

        card_layout.addWidget(
            self.login_btn
        )

        card_layout.addWidget(
            self.register_btn
        )

        root.addLayout(left, 1)
        root.addWidget(card)
                # ===========================
        # EVENTS
        # ===========================

        self.login_btn.clicked.connect(
            self.login
        )

        self.register_btn.clicked.connect(
            self.open_register
        )

        self.password.returnPressed.connect(
            self.login
        )

    # ======================================
    # LOGIN
    # ======================================

    def login(self):

        email = self.email.text().strip()
        password = self.password.text()

        # Validation

        if email == "":
            QMessageBox.warning(
                self,
                "Email Required",
                "Please enter your email."
            )
            return

        if password == "":
            QMessageBox.warning(
                self,
                "Password Required",
                "Please enter your password."
            )
            return

        # Database Login

        success = AuthService.login_user(
            email,
            password
        )

        if success:

            QMessageBox.information(
                self,
                "Success",
                "Login Successful!"
            )

            try:

                print("Creating Dashboard...")

                self.dashboard = DashboardWindow()

                print("Showing Dashboard...")

                self.dashboard.show()

                print("Closing Login Window...")

                self.close()

            except Exception as e:

                import traceback
                traceback.print_exc()

                QMessageBox.critical(
                    self,
                    "Dashboard Error",
                    str(e)
                )

        else:

            QMessageBox.warning(
                self,
                "Login Failed",
                "Invalid Email or Password."
            )

    # ======================================
    # OPEN REGISTER
    # ======================================

    def open_register(self):

        self.register_window = RegisterWindow()

        self.register_window.show()

        self.close()