from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
)


class TopBar(QWidget):

    def __init__(self):
        super().__init__()

        self.setFixedHeight(70)

        self.setStyleSheet("""
            QWidget{
                background:#111827;
                color:white;
                font-family:Segoe UI;
            }

            QLabel{
                font-size:20px;
                font-weight:bold;
            }

            QLineEdit{
                padding:8px;
                border:2px solid #2563EB;
                border-radius:8px;
                background:#1E293B;
                color:white;
                font-size:14px;
            }

            QPushButton{
                background:#2563EB;
                color:white;
                border:none;
                border-radius:8px;
                padding:8px 15px;
                font-size:14px;
                font-weight:bold;
            }

            QPushButton:hover{
                background:#1D4ED8;
            }
        """)

        layout = QHBoxLayout()

        self.title = QLabel("🚀 NEXUS AI Dashboard")

        self.search = QLineEdit()
        self.search.setPlaceholderText("Search...")

        self.user_btn = QPushButton("👤 User")

        layout.addWidget(self.title)
        layout.addStretch()
        layout.addWidget(self.search)
        layout.addWidget(self.user_btn)

        self.setLayout(layout)