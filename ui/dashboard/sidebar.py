from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QCursor
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
                background:#0F172A;
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
                padding:12px 16px;
                font-size:15px;
                border-radius:10px;
            }

            QPushButton:hover{
                background:#1E293B;
            }
        """)

        layout = QVBoxLayout()
        layout.setContentsMargins(10, 15, 10, 15)
        layout.setSpacing(8)

        title = QLabel("🤖 NEXUS AI")
        title.setAlignment(Qt.AlignCenter)

        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setStyleSheet("color:#334155;")

        layout.addWidget(title)
        layout.addWidget(line)

        self.buttons = {}

        self.chat_btn = self.create_button("💬 AI Chat", "chat")
        self.project_btn = self.create_button("📁 Projects", "projects")
        self.explorer_btn = self.create_button("📂 Explorer", "explorer")
        self.editor_btn = self.create_button("📝 Code Editor", "editor")
        self.agent_btn = self.create_button("🤖 AI Agent", "agent")
        self.memory_btn = self.create_button("🧠 Memory", "memory")
        self.settings_btn = self.create_button("⚙ Settings", "settings")
        self.logout_btn = self.create_button("🚪 Logout", "logout")

        layout.addWidget(self.chat_btn)
        layout.addWidget(self.project_btn)
        layout.addWidget(self.explorer_btn)
        layout.addWidget(self.editor_btn)
        layout.addWidget(self.agent_btn)
        layout.addWidget(self.memory_btn)

        layout.addStretch()

        layout.addWidget(self.settings_btn)
        layout.addWidget(self.logout_btn)

        self.setLayout(layout)

        # Default Active Button
        self.set_active("chat")

    def create_button(self, text, key):

        btn = QPushButton(text)
        btn.setCursor(QCursor(Qt.PointingHandCursor))

        btn.clicked.connect(lambda: self.button_clicked(key))

        self.buttons[key] = btn

        return btn

    def button_clicked(self, key):

        self.set_active(key)
        self.menu_clicked.emit(key)

    def set_active(self, active_key):

        for key, btn in self.buttons.items():

            if key == active_key:
                btn.setStyleSheet("""
                    QPushButton{
                        background:#2563EB;
                        color:white;
                        border-radius:10px;
                        padding:12px 16px;
                        font-size:15px;
                        font-weight:bold;
                        text-align:left;
                    }
                """)
            else:
                btn.setStyleSheet("""
                    QPushButton{
                        background:transparent;
                        color:white;
                        border:none;
                        border-radius:10px;
                        padding:12px 16px;
                        font-size:15px;
                        text-align:left;
                    }

                    QPushButton:hover{
                        background:#1E293B;
                    }
                """)