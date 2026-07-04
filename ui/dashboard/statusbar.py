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

        layout = QHBoxLayout(self)

        layout.setContentsMargins(15, 0, 15, 0)
        layout.setSpacing(10)

        # Left Status
        self.left_status = QLabel("🟢 Ready")
        layout.addWidget(self.left_status)

        layout.addStretch()

        # Right Status
        self.right_status = QLabel("NEXUS AI v1.0")
        layout.addWidget(self.right_status)

    # ======================================
    # Main Status Methods
    # ======================================

    def set_status(self, text: str):
        self.left_status.setText(text)

    def set_version(self, version: str):
        self.right_status.setText(version)

    # ======================================
    # Compatibility Methods
    # (Works like QStatusBar)
    # ======================================

    def showMessage(self, text, timeout=0):
        """
        Compatible with QStatusBar.showMessage()
        """
        self.left_status.setText(text)

    def clearMessage(self):
        self.left_status.setText("🟢 Ready")

    def currentMessage(self):
        return self.left_status.text()

    # ======================================
    # Helper Methods
    # ======================================

    def set_ready(self):
        self.left_status.setText("🟢 Ready")

    def set_busy(self):
        self.left_status.setText("🟡 Processing...")

    def set_error(self):
        self.left_status.setText("🔴 Error")

    def set_success(self):
        self.left_status.setText("✅ Success")

    def set_warning(self):
        self.left_status.setText("⚠ Warning")

    def set_info(self):
        self.left_status.setText("ℹ Information")