from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
    QCheckBox,
    QMessageBox
)

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

from auth.auth_service import AuthService
from ui.dashboard.dashboard_window import DashboardWindow
from ui.login.register_window import RegisterWindow


class LoginWindow(QWidget):

    def __init__(self):
        super().__init__()

        # ==========================================
        # WINDOW
        # ==========================================

        self.setWindowTitle("🤖 NEXUS AI")

        self.resize(1350, 760)

        self.setMinimumSize(1200,700)

        # ==========================================
        # THEME
        # ==========================================

        self.setStyleSheet("""

        QWidget{

            background:#0F172A;

            color:white;

            font-family:'Segoe UI';

        }

        #loginCard{

            background:#1E293B;

            border:1px solid #334155;

            border-radius:24px;

        }

        QLabel{

            background:transparent;

            color:white;

        }

        QLineEdit{

            background:#111827;

            border:2px solid #334155;

            border-radius:14px;

            padding:14px;

            font-size:15px;

        }

        QLineEdit:focus{

            border:2px solid #3B82F6;

        }

        QPushButton{

            background:#2563EB;

            border:none;

            border-radius:14px;

            padding:14px;

            font-size:15px;

            font-weight:bold;

            color:white;

        }

        QPushButton:hover{

            background:#3B82F6;

        }

        QCheckBox{

            font-size:14px;

        }

        """)

        # ==========================================
        # ROOT LAYOUT
        # ==========================================

        self.root = QHBoxLayout(self)

        self.root.setContentsMargins(
            60,
            40,
            60,
            40
        )

        self.root.setSpacing(80)

        # ==========================================
        # LEFT PANEL
        # ==========================================

        self.left = QVBoxLayout()

        self.left.setAlignment(Qt.AlignCenter)
                # ==========================================
        # LOGO
        # ==========================================

        logo = QLabel("🤖")
        logo.setAlignment(Qt.AlignCenter)
        logo.setFont(QFont("Segoe UI Emoji", 90))

        # ==========================================
        # TITLE
        # ==========================================

        title = QLabel("NEXUS AI")

        title.setAlignment(Qt.AlignCenter)

        title.setStyleSheet("""

            font-size:56px;

            font-weight:800;

            color:#60A5FA;

        """)

        # ==========================================
        # SUBTITLE
        # ==========================================

        subtitle = QLabel(
            "Your Personal AI Assistant"
        )

        subtitle.setAlignment(Qt.AlignCenter)

        subtitle.setStyleSheet("""

            font-size:20px;

            color:#94A3B8;

        """)

        # ==========================================
        # DESCRIPTION
        # ==========================================

        description = QLabel(

            "Experience the next generation of\n"
            "Artificial Intelligence.\n\n"
            "💬 Chat Naturally\n"
            "💻 Generate Code\n"
            "📄 Summarize Documents\n"
            "🧠 Learn Faster\n"
            "🚀 Build Projects"

        )

        description.setAlignment(Qt.AlignCenter)

        description.setStyleSheet("""

            font-size:15px;

            color:#CBD5E1;

            line-height:24px;

        """)

        # ==========================================
        # VERSION
        # ==========================================

        version = QLabel("Version 1.0")

        version.setAlignment(Qt.AlignCenter)

        version.setStyleSheet("""

            color:#64748B;

            font-size:13px;

        """)

        # ==========================================
        # ADD LEFT PANEL
        # ==========================================

        self.left.addStretch()

        self.left.addWidget(logo)

        self.left.addSpacing(15)

        self.left.addWidget(title)

        self.left.addSpacing(8)

        self.left.addWidget(subtitle)

        self.left.addSpacing(25)

        self.left.addWidget(description)

        self.left.addStretch()

        self.left.addWidget(version)
                # ==========================================
        # LOGO
        # ==========================================

        logo = QLabel("🤖")
        logo.setAlignment(Qt.AlignCenter)
        logo.setFont(QFont("Segoe UI Emoji", 90))

        # ==========================================
        # TITLE
        # ==========================================

        title = QLabel("NEXUS AI")

        title.setAlignment(Qt.AlignCenter)

        title.setStyleSheet("""

            font-size:56px;

            font-weight:800;

            color:#60A5FA;

        """)

        # ==========================================
        # SUBTITLE
        # ==========================================

        subtitle = QLabel(
            "Your Personal AI Assistant"
        )

        subtitle.setAlignment(Qt.AlignCenter)

        subtitle.setStyleSheet("""

            font-size:20px;

            color:#94A3B8;

        """)

        # ==========================================
        # DESCRIPTION
        # ==========================================

        description = QLabel(

            "Experience the next generation of\n"
            "Artificial Intelligence.\n\n"
            "💬 Chat Naturally\n"
            "💻 Generate Code\n"
            "📄 Summarize Documents\n"
            "🧠 Learn Faster\n"
            "🚀 Build Projects"

        )

        description.setAlignment(Qt.AlignCenter)

        description.setStyleSheet("""

            font-size:15px;

            color:#CBD5E1;

            line-height:24px;

        """)

        # ==========================================
        # VERSION
        # ==========================================

        version = QLabel("Version 1.0")

        version.setAlignment(Qt.AlignCenter)

        version.setStyleSheet("""

            color:#64748B;

            font-size:13px;

        """)

        # ==========================================
        # ADD LEFT PANEL
        # ==========================================

        self.left.addStretch()

        self.left.addWidget(logo)

        self.left.addSpacing(15)

        self.left.addWidget(title)

        self.left.addSpacing(8)

        self.left.addWidget(subtitle)

        self.left.addSpacing(25)

        self.left.addWidget(description)

        self.left.addStretch()

        self.left.addWidget(version)
                # ==========================================
        # EVENTS
        # ==========================================

        self.login_btn.clicked.connect(self.login)
        self.register_btn.clicked.connect(self.open_register)

        self.email.returnPressed.connect(self.login)
        self.password.returnPressed.connect(self.login)

    # ==========================================
    # LOGIN
    # ==========================================

    def login(self):

        email = self.email.text().strip()
        password = self.password.text()

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

        print("Closing Login...")
        self.close()

    except Exception as e:

        print("Dashboard Error:", e)

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

    # ==========================================
    # OPEN REGISTER
    # ==========================================

    def open_register(self):

        self.register = RegisterWindow()

        self.register.show()

        self.close()