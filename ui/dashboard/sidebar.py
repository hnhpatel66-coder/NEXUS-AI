from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QFrame,
)


class Sidebar(QWidget):

    menu_clicked = Signal(str)

    def __init__(self):
        super().__init__()

        self.setFixedWidth(220)

        self.setStyleSheet("""
            QWidget{
                background-color:#0F172A;
                color:white;
                font-family:Segoe UI;
            }

            QLabel{
                font-size:22px;
                font-weight:bold;
                padding:15px;
            }

            QPushButton{
                background:transparent;
                border:none;
                color:white;
                text-align:left;
                padding:12px;
                font-size:15px;
                border-radius:8px;
            }

            QPushButton:hover{
                background:#1E293B;
            }

            QPushButton:pressed{
                background:#2563EB;
            }
        """)

        layout = QVBoxLayout()

        title = QLabel("🤖 NEXUS AI")
        title.setAlignment(Qt.AlignCenter)

        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setStyleSheet("color:#334155;")

        layout.addWidget(title)
        layout.addWidget(line)

        self.chat_btn = QPushButton("💬 AI Chat")
        self.project_btn = QPushButton("📁 Projects")
        self.explorer_btn = QPushButton("📂 Explorer")
        self.editor_btn = QPushButton("📝 Code Editor")
        self.agent_btn = QPushButton("🤖 AI Agent")
        self.memory_btn = QPushButton("🧠 Memory")
        self.settings_btn = QPushButton("⚙ Settings")

        layout.addWidget(self.chat_btn)
        layout.addWidget(self.project_btn)
        layout.addWidget(self.explorer_btn)
        layout.addWidget(self.editor_btn)
        layout.addWidget(self.agent_btn)
        layout.addWidget(self.memory_btn)

        layout.addStretch()

        layout.addWidget(self.settings_btn)

        self.logout_btn = QPushButton("🚪 Logout")
        layout.addWidget(self.logout_btn)

        self.setLayout(layout)

        self.chat_btn.clicked.connect(
            lambda: self.menu_clicked.emit("chat")
        )

        self.project_btn.clicked.connect(
            lambda: self.menu_clicked.emit("projects")
        )

        self.explorer_btn.clicked.connect(
            lambda: self.menu_clicked.emit("explorer")
        )

        self.editor_btn.clicked.connect(
            lambda: self.menu_clicked.emit("editor")
        )

        self.agent_btn.clicked.connect(
            lambda: self.menu_clicked.emit("agent")
        )

        self.memory_btn.clicked.connect(
            lambda: self.menu_clicked.emit("memory")
        )

        self.settings_btn.clicked.connect(
            lambda: self.menu_clicked.emit("settings")
        )

        self.logout_btn.clicked.connect(
            lambda: self.menu_clicked.emit("logout")
        )