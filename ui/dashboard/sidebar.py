from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QFrame,
)

from PySide6.QtCore import (
    Qt,
    Signal,
)

from PySide6.QtGui import (
    QCursor,
)


class Sidebar(QWidget):

    menu_clicked = Signal(str)

    def __init__(self):
        super().__init__()

        self.setFixedWidth(250)

        self.setStyleSheet("""

        QWidget{

            background:#0B1220;

            color:white;

            font-family:'Segoe UI';

        }

        QLabel{

            background:transparent;

        }

        QFrame{

            background:transparent;

        }

        QPushButton{

            background:transparent;

            color:#CBD5E1;

            border:none;

            border-radius:12px;

            padding:14px 18px;

            text-align:left;

            font-size:15px;

            font-weight:500;

        }

        QPushButton:hover{

            background:#1E293B;

            color:white;

        }

        """)

        self.buttons = {}

        self.layout = QVBoxLayout(self)

        self.layout.setContentsMargins(
            16,
            20,
            16,
            20
        )

        self.layout.setSpacing(8)

        # ============================
        # LOGO
        # ============================

        self.logo = QLabel("🤖 NEXUS AI")

        self.logo.setAlignment(
            Qt.AlignCenter
        )

        self.logo.setStyleSheet("""

        font-size:24px;

        font-weight:bold;

        color:#60A5FA;

        """)

        self.layout.addWidget(
            self.logo
        )

        self.layout.addSpacing(15)

        line = QFrame()

        line.setFrameShape(
            QFrame.HLine
        )

        line.setStyleSheet("""
        color:#334155;
        """)

        self.layout.addWidget(line)

        self.layout.addSpacing(10)
                # ============================
        # MENU BUTTONS
        # ============================

        self.home_btn = self.create_button(
            "🏠  Home",
            "home"
        )

        self.chat_btn = self.create_button(
            "💬  AI Chat",
            "chat"
        )

        self.projects_btn = self.create_button(
            "📁  Projects",
            "projects"
        )

        self.explorer_btn = self.create_button(
            "📂  Explorer",
            "explorer"
        )

        self.editor_btn = self.create_button(
            "📝  Code Editor",
            "editor"
        )

        self.agent_btn = self.create_button(
            "🤖  AI Agent",
            "agent"
        )

        self.memory_btn = self.create_button(
            "🧠  Memory",
            "memory"
        )

        self.settings_btn = self.create_button(
            "⚙️  Settings",
            "settings"
        )

        self.logout_btn = self.create_button(
            "🚪  Logout",
            "logout"
        )

        self.layout.addWidget(self.home_btn)
        self.layout.addWidget(self.chat_btn)
        self.layout.addWidget(self.projects_btn)
        self.layout.addWidget(self.explorer_btn)
        self.layout.addWidget(self.editor_btn)
        self.layout.addWidget(self.agent_btn)
        self.layout.addWidget(self.memory_btn)

        self.layout.addStretch()

        self.layout.addWidget(self.settings_btn)
        self.layout.addSpacing(10)
        self.layout.addWidget(self.logout_btn)

        # Default Active
        self.set_active("home")
            # ==========================================
    # CREATE BUTTON
    # ==========================================

    def create_button(self, text: str, key: str):

        button = QPushButton(text)

        button.setCursor(
            QCursor(Qt.PointingHandCursor)
        )

        button.clicked.connect(
            lambda: self.button_clicked(key)
        )

        self.buttons[key] = button

        return button

    # ==========================================
    # BUTTON CLICK
    # ==========================================

    def button_clicked(self, key: str):

        self.set_active(key)

        self.menu_clicked.emit(key)

    # ==========================================
    # ACTIVE MENU
    # ==========================================

    def set_active(self, active_key):

        active_style = """
        QPushButton{

            background:#2563EB;

            color:white;

            border:none;

            border-radius:12px;

            padding:14px 18px;

            text-align:left;

            font-size:15px;

            font-weight:bold;

        }

        QPushButton:hover{

            background:#3B82F6;

        }
        """

        normal_style = """
        QPushButton{

            background:transparent;

            color:#CBD5E1;

            border:none;

            border-radius:12px;

            padding:14px 18px;

            text-align:left;

            font-size:15px;

            font-weight:500;

        }

        QPushButton:hover{

            background:#1E293B;

            color:white;

        }
        """

        for key, button in self.buttons.items():

            if key == active_key:

                button.setStyleSheet(
                    active_style
                )

            else:

                button.setStyleSheet(
                    normal_style
                )

    # ==========================================
    # PUBLIC METHODS
    # ==========================================

    def select_home(self):
        self.button_clicked("home")

    def select_chat(self):
        self.button_clicked("chat")

    def select_projects(self):
        self.button_clicked("projects")

    def select_explorer(self):
        self.button_clicked("explorer")

    def select_editor(self):
        self.button_clicked("editor")

    def select_agent(self):
        self.button_clicked("agent")

    def select_memory(self):
        self.button_clicked("memory")

    def select_settings(self):
        self.button_clicked("settings")