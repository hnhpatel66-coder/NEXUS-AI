from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QStackedWidget,
)

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
        self.resize(1400, 850)

        self.setStyleSheet("""
            QMainWindow{
                background:#111827;
            }
        """)

        # ===========================
        # Central Widget
        # ===========================

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # ===========================
        # Sidebar
        # ===========================

        self.sidebar = Sidebar()

        # ===========================
        # Right Layout
        # ===========================

        right_layout = QVBoxLayout()
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(0)

        self.topbar = TopBar()

        # ===========================
        # Pages
        # ===========================

        self.home = HomePage()
        self.chat = ChatPage()
        self.projects = ProjectsPage()
        self.explorer = ExplorerPage()
        self.editor = EditorPage()
        self.agent = AgentPage()
        self.memory = MemoryPage()
        self.settings = SettingsPage()

        # ===========================
        # Stacked Widget
        # ===========================

        self.stack = QStackedWidget()

        self.stack.addWidget(self.home)        # 0
        self.stack.addWidget(self.chat)        # 1
        self.stack.addWidget(self.projects)    # 2
        self.stack.addWidget(self.explorer)    # 3
        self.stack.addWidget(self.editor)      # 4
        self.stack.addWidget(self.agent)       # 5
        self.stack.addWidget(self.memory)      # 6
        self.stack.addWidget(self.settings)    # 7

        # ===========================
        # Status Bar
        # ===========================

        self.status = StatusBar()

        right_layout.addWidget(self.topbar)
        right_layout.addWidget(self.stack)
        right_layout.addWidget(self.status)

        main_layout.addWidget(self.sidebar)
        main_layout.addLayout(right_layout)

        central_widget.setLayout(main_layout)

        # Sidebar Signal
        self.sidebar.menu_clicked.connect(self.menu_action)

    def menu_action(self, menu):

        if menu == "chat":
            self.stack.setCurrentIndex(1)

        elif menu == "projects":
            self.stack.setCurrentIndex(2)

        elif menu == "explorer":
            self.stack.setCurrentIndex(3)

        elif menu == "editor":
            self.stack.setCurrentIndex(4)

        elif menu == "agent":
            self.stack.setCurrentIndex(5)

        elif menu == "memory":
            self.stack.setCurrentIndex(6)

        elif menu == "settings":
            self.stack.setCurrentIndex(7)

        elif menu == "logout":
            self.close()