from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox,
)

from ui.dashboard.sidebar import Sidebar
from ui.dashboard.topbar import TopBar
from ui.dashboard.home_page import HomePage
from ui.dashboard.statusbar import StatusBar


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

        # Main Widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Main Horizontal Layout
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Sidebar
        self.sidebar = Sidebar()

        # Right Side Layout
        right_layout = QVBoxLayout()
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(0)

        # Top Bar
        self.topbar = TopBar()

        # Home Page
        self.home = HomePage()

        # Status Bar
        self.status = StatusBar()

        right_layout.addWidget(self.topbar)
        right_layout.addWidget(self.home)
        right_layout.addWidget(self.status)

        main_layout.addWidget(self.sidebar)
        main_layout.addLayout(right_layout)

        central_widget.setLayout(main_layout)

        # Sidebar Events
        self.sidebar.menu_clicked.connect(self.menu_action)

    def menu_action(self, menu):

        if menu == "chat":
            QMessageBox.information(
                self,
                "AI Chat",
                "AI Chat module will be available in Phase 5."
            )

        elif menu == "projects":
            QMessageBox.information(
                self,
                "Projects",
                "Project Manager is coming soon."
            )

        elif menu == "explorer":
            QMessageBox.information(
                self,
                "Explorer",
                "File Explorer is under development."
            )

        elif menu == "editor":
            QMessageBox.information(
                self,
                "Code Editor",
                "Professional Code Editor coming soon."
            )

        elif menu == "agent":
            QMessageBox.information(
                self,
                "AI Agent",
                "AI Agent will be added in future phase."
            )

        elif menu == "memory":
            QMessageBox.information(
                self,
                "Memory",
                "Memory Manager is under development."
            )

        elif menu == "settings":
            QMessageBox.information(
                self,
                "Settings",
                "Settings Panel coming soon."
            )

        elif menu == "logout":
            self.close()