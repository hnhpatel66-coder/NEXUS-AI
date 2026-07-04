from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QStackedWidget,
)

from PySide6.QtCore import Qt

from ui.dashboard.sidebar import Sidebar
from ui.dashboard.topbar import TopBar
from ui.dashboard.statusbar import StatusBar

from ui.dashboard.home_page import HomePage
from ui.dashboard.chat_page import ChatPage
from ui.dashboard.projects_page import ProjectsPage
from ui.dashboard.explorer_page import ExplorerPage
from ui.dashboard.editor_page import EditorPage
from ui.dashboard.agent_page import AgentPage
from ui.dashboard.memory_page import MemoryPage
from ui.dashboard.settings_page import SettingsPage


class DashboardWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("NEXUS AI")

        self.resize(1450, 900)

        self.setMinimumSize(1200, 750)

        self.setStyleSheet("""

        QMainWindow{

            background:#111827;

        }

        """)

        # =====================================
        # CENTRAL WIDGET
        # =====================================

        self.central = QWidget()

        self.setCentralWidget(self.central)

        # =====================================
        # MAIN LAYOUT
        # =====================================

        self.main_layout = QHBoxLayout(self.central)

        self.main_layout.setContentsMargins(
            0,
            0,
            0,
            0
        )

        self.main_layout.setSpacing(0)

        # =====================================
        # SIDEBAR
        # =====================================

        self.sidebar = Sidebar()

        self.main_layout.addWidget(
            self.sidebar
        )

        # =====================================
        # RIGHT SIDE
        # =====================================

        self.right_widget = QWidget()

        self.right_layout = QVBoxLayout(
            self.right_widget
        )

        self.right_layout.setContentsMargins(
            0,
            0,
            0,
            0
        )

        self.right_layout.setSpacing(0)

        # =====================================
        # TOPBAR
        # =====================================

        self.topbar = TopBar()

        self.right_layout.addWidget(
            self.topbar
        )

        # =====================================
        # STACK
        # =====================================

        self.stack = QStackedWidget()

        self.stack.setStyleSheet("""

        QStackedWidget{

            background:#0F172A;

        }

        """)

        self.right_layout.addWidget(
            self.stack
        )

        # =====================================
        # STATUS BAR
        # =====================================

        self.status = StatusBar()

        self.right_layout.addWidget(
            self.status
        )

        self.main_layout.addWidget(
            self.right_widget
        )
                # =====================================
        # CREATE PAGES
        # =====================================

        self.home_page = HomePage()
        self.chat_page = ChatPage()
        self.projects_page = ProjectsPage()
        self.explorer_page = ExplorerPage()
        self.editor_page = EditorPage()
        self.agent_page = AgentPage()
        self.memory_page = MemoryPage()
        self.settings_page = SettingsPage()

        # =====================================
        # ADD PAGES TO STACK
        # =====================================

        self.stack.addWidget(self.home_page)       # Index 0
        self.stack.addWidget(self.chat_page)       # Index 1
        self.stack.addWidget(self.projects_page)   # Index 2
        self.stack.addWidget(self.explorer_page)   # Index 3
        self.stack.addWidget(self.editor_page)     # Index 4
        self.stack.addWidget(self.agent_page)      # Index 5
        self.stack.addWidget(self.memory_page)     # Index 6
        self.stack.addWidget(self.settings_page)   # Index 7

        # Default Page
        self.stack.setCurrentIndex(0)

        # =====================================
        # CONNECT SIDEBAR
        # =====================================

        self.sidebar.menu_clicked.connect(
            self.change_page
        )

        # =====================================
        # WINDOW READY
        # =====================================

        self.status.showMessage(
            "Dashboard Loaded Successfully"
        )
            # =====================================
    # CHANGE PAGE
    # =====================================

    def change_page(self, menu):

        page_map = {
            "home": 0,
            "chat": 1,
            "projects": 2,
            "explorer": 3,
            "editor": 4,
            "agent": 5,
            "memory": 6,
            "settings": 7,
        }

        if menu in page_map:

            self.stack.setCurrentIndex(
                page_map[menu]
            )

            self.status.showMessage(
                f"{menu.title()} Opened"
            )

            return

        # =================================
        # LOGOUT
        # =================================

        if menu == "logout":

            from PySide6.QtWidgets import QMessageBox

            reply = QMessageBox.question(

                self,

                "Logout",

                "Are you sure you want to logout?",

                QMessageBox.Yes | QMessageBox.No

            )

            if reply == QMessageBox.Yes:

                from ui.login.login_window import LoginWindow

                self.login_window = LoginWindow()

                self.login_window.show()

                self.close()

    # =====================================
    # SHOW MESSAGE IN STATUSBAR
    # =====================================

    def set_status(self, text):

        self.status.showMessage(text)

    # =====================================
    # OPEN CHAT
    # =====================================

    def open_chat(self):

        self.stack.setCurrentIndex(1)

        self.status.showMessage(
            "AI Chat Ready"
        )

    # =====================================
    # OPEN HOME
    # =====================================

    def open_home(self):

        self.stack.setCurrentIndex(0)

        self.status.showMessage(
            "Welcome Home"
        )

    # =====================================
    # WINDOW CLOSE EVENT
    # =====================================

    def closeEvent(self, event):

        print("Dashboard Closed")

        event.accept()