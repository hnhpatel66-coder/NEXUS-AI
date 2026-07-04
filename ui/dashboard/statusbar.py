from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QLabel,
)

from PySide6.QtCore import Qt


class StatusBar(QWidget):

    def __init__(self):
        super().__init__()

        self.setFixedHeight(35)

        self.setStyleSheet("""

        QWidget{

            background:#0B1220;

            color:#94A3B8;

            font-family:'Segoe UI';

            border-top:1px solid #1E293B;

        }

        QLabel{

            background:transparent;

            font-size:12px;

        }

        """)

        self.layout = QHBoxLayout(self)

        self.layout.setContentsMargins(
            15,
            0,
            15,
            0
        )

        self.layout.setSpacing(10)

        # =====================================
        # LEFT STATUS
        # =====================================

        self.left_status = QLabel("🟢 Ready")

        self.layout.addWidget(self.left_status)

        self.layout.addStretch()

        # =====================================
        # RIGHT STATUS
        # =====================================

        self.right_status = QLabel("NEXUS AI v1.0")

        self.layout.addWidget(self.right_status)

    # =====================================
    # UPDATE LEFT STATUS
    # =====================================

    def set_status(self, text: str):

        self.left_status.setText(text)

    # =====================================
    # UPDATE RIGHT STATUS
    # =====================================

    def set_version(self, text: str):

        self.right_status.setText(text)

    # =====================================
    # READY / BUSY STATES
    # =====================================

    def set_ready(self):

        self.left_status.setText("🟢 Ready")

    def set_busy(self):

        self.left_status.setText("🟡 Processing...")

    def set_error(self):

        self.left_status.setText("🔴 Error")