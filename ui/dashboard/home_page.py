from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QGridLayout,
    QFrame,
    QPushButton,
)


class HomePage(QWidget):

    def __init__(self):
        super().__init__()

        self.setStyleSheet("""
            QWidget{
                background:#111827;
                color:white;
                font-family:Segoe UI;
            }

            QLabel#title{
                font-size:28px;
                font-weight:bold;
            }

            QLabel#subtitle{
                font-size:14px;
                color:#9CA3AF;
            }

            QFrame{
                background:#1E293B;
                border:1px solid #334155;
                border-radius:16px;
            }

            QFrame:hover{
                border:2px solid #3B82F6;
                background:#243244;
            }

            QLabel.cardTitle{
                font-size:18px;
                font-weight:bold;
                border:none;
            }

            QLabel.cardText{
                font-size:13px;
                color:#CBD5E1;
                border:none;
            }

            QPushButton{
                background:#2563EB;
                color:white;
                border:none;
                border-radius:8px;
                padding:8px;
                font-size:13px;
                font-weight:bold;
            }

            QPushButton:hover{
                background:#1D4ED8;
            }
        """)

        main_layout = QVBoxLayout()

        title = QLabel("👋 Welcome to NEXUS AI")
        title.setObjectName("title")

        subtitle = QLabel(
            "Your Personal AI Assistant & Development Workspace"
        )
        subtitle.setObjectName("subtitle")

        main_layout.addWidget(title)
        main_layout.addWidget(subtitle)
        main_layout.addSpacing(25)

        grid = QGridLayout()
        grid.setHorizontalSpacing(20)
        grid.setVerticalSpacing(20)

        grid.addWidget(
            self.create_card(
                "💬 AI Chat",
                "Start chatting with your AI assistant."
            ),
            0,
            0
        )

        grid.addWidget(
            self.create_card(
                "📁 Projects",
                "Manage your AI and coding projects."
            ),
            0,
            1
        )

        grid.addWidget(
            self.create_card(
                "🤖 AI Agent",
                "Launch smart automation tasks."
            ),
            1,
            0
        )

        grid.addWidget(
            self.create_card(
                "🧠 Memory",
                "View saved memories and history."
            ),
            1,
            1
        )

        main_layout.addLayout(grid)
        main_layout.addStretch()

        self.setLayout(main_layout)

    def create_card(self, title_text, body_text):

        card = QFrame()
        card.setMinimumHeight(180)

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(12)

        title = QLabel(title_text)
        title.setProperty("class", "cardTitle")

        body = QLabel(body_text)
        body.setWordWrap(True)
        body.setProperty("class", "cardText")

        button = QPushButton("Open →")

        layout.addWidget(title)
        layout.addWidget(body)

        layout.addStretch()

        layout.addWidget(button)

        card.setLayout(layout)

        return card