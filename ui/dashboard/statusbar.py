from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QHBoxLayout,
)


class StatusBar(QWidget):

    def __init__(self):
        super().__init__()

        self.setFixedHeight(35)

        self.setStyleSheet("""
            QWidget{
                background:#0F172A;
                color:white;
                font-family:Segoe UI;
            }

            QLabel{
                font-size:12px;
                padding:5px;
            }
        """)

        layout = QHBoxLayout()

        self.status = QLabel("🟢 Ready")
        self.ai_status = QLabel("🤖 AI : Offline")
        self.workspace = QLabel("📁 Workspace : NEXUS-AI")

        layout.addWidget(self.status)
        layout.addStretch()
        layout.addWidget(self.ai_status)
        layout.addWidget(self.workspace)

        self.setLayout(layout)