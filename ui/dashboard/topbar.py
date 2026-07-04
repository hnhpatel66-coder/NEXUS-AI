from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
)

from PySide6.QtCore import (
    Qt,
    QTimer,
    QTime,
)

from PySide6.QtGui import (
    QCursor,
)


class TopBar(QWidget):

    def __init__(self):
        super().__init__()

        self.setFixedHeight(70)

        self.setStyleSheet("""

        QWidget{

            background:#111827;

            color:white;

            font-family:'Segoe UI';

            border-bottom:1px solid #1E293B;

        }

        QLabel{

            background:transparent;

        }

        QLineEdit{

            background:#1E293B;

            color:white;

            border:1px solid #334155;

            border-radius:12px;

            padding:10px 14px;

            font-size:14px;

        }

        QLineEdit:focus{

            border:1px solid #3B82F6;

        }

        QPushButton{

            background:#2563EB;

            color:white;

            border:none;

            border-radius:10px;

            padding:10px 18px;

            font-size:14px;

            font-weight:bold;

        }

        QPushButton:hover{

            background:#3B82F6;

        }

        """)

        self.layout = QHBoxLayout(self)

        self.layout.setContentsMargins(
            20,
            10,
            20,
            10
        )

        self.layout.setSpacing(15)
                # ==========================================
        # LEFT : PAGE TITLE
        # ==========================================

        self.title = QLabel("🏠 Dashboard")

        self.title.setStyleSheet("""

        font-size:24px;

        font-weight:bold;

        color:#60A5FA;

        """)

        self.layout.addWidget(self.title)

        self.layout.addStretch()

        # ==========================================
        # SEARCH BOX
        # ==========================================

        self.search = QLineEdit()

        self.search.setFixedWidth(320)

        self.search.setPlaceholderText(
            "🔍 Search anything..."
        )

        self.layout.addWidget(self.search)

        # ==========================================
        # CLOCK
        # ==========================================

        self.clock = QLabel()

        self.clock.setAlignment(Qt.AlignCenter)

        self.clock.setStyleSheet("""

        font-size:14px;

        color:#CBD5E1;

        font-weight:bold;

        """)

        self.layout.addWidget(self.clock)

        # ==========================================
        # USER BUTTON
        # ==========================================

        self.user_btn = QPushButton("👤 Nirbhay")

        self.user_btn.setCursor(
            QCursor(Qt.PointingHandCursor)
        )

        self.layout.addWidget(self.user_btn)

        # ==========================================
        # TIMER
        # ==========================================

        self.timer = QTimer(self)

        self.timer.timeout.connect(
            self.update_clock
        )

        self.timer.start(1000)

        self.update_clock()
            # ==========================================
    # UPDATE LIVE CLOCK
    # ==========================================

    def update_clock(self):

        current_time = QTime.currentTime()

        self.clock.setText(
            current_time.toString("hh:mm:ss AP")
        )

    # ==========================================
    # CHANGE PAGE TITLE
    # ==========================================

    def set_title(self, title: str):

        self.title.setText(title)

    # ==========================================
    # CHANGE USER NAME
    # ==========================================

    def set_username(self, username: str):

        if username.strip():

            self.user_btn.setText(
                f"👤 {username}"
            )

    # ==========================================
    # GET SEARCH TEXT
    # ==========================================

    def search_text(self):

        return self.search.text().strip()

    # ==========================================
    # CLEAR SEARCH
    # ==========================================

    def clear_search(self):

        self.search.clear()

    # ==========================================
    # ENABLE / DISABLE SEARCH
    # ==========================================

    def enable_search(self, enabled=True):

        self.search.setEnabled(enabled)

    # ==========================================
    # SET SEARCH PLACEHOLDER
    # ==========================================

    def set_placeholder(self, text):

        self.search.setPlaceholderText(text)

    # ==========================================
    # FOCUS SEARCH
    # ==========================================

    def focus_search(self):

        self.search.setFocus()