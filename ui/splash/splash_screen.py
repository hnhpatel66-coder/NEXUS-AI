from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QProgressBar,
)

from PySide6.QtCore import (
    Qt,
    QTimer,
)

from PySide6.QtGui import (
    QFont,
)

from ui.login.login_window import LoginWindow


class SplashScreen(QWidget):

    def __init__(self):
        super().__init__()

        self.login_window = None

        self.setWindowTitle("NEXUS AI")
        self.setFixedSize(700, 420)

        self.setWindowFlag(Qt.FramelessWindowHint)

        self.setStyleSheet("""

        QWidget{
            background:#0F172A;
            color:white;
            font-family:'Segoe UI';
        }

        QLabel{
            background:transparent;
            color:white;
        }

        QProgressBar{

            border:none;

            background:#1E293B;

            border-radius:10px;

            text-align:center;

            color:white;

            height:18px;

        }

        QProgressBar::chunk{

            background:#2563EB;

            border-radius:10px;

        }

        """)

        layout = QVBoxLayout(self)

        layout.setContentsMargins(
            60,
            60,
            60,
            60
        )

        layout.addStretch()

        # ==========================
        # LOGO
        # ==========================

        logo = QLabel("🤖")

        logo.setAlignment(Qt.AlignCenter)

        logo.setFont(
            QFont("Segoe UI Emoji", 70)
        )

        # ==========================
        # TITLE
        # ==========================

        title = QLabel("NEXUS AI")

        title.setAlignment(Qt.AlignCenter)

        title.setStyleSheet("""

        font-size:42px;

        font-weight:bold;

        color:#60A5FA;

        """)

        subtitle = QLabel(
            "Initializing Artificial Intelligence..."
        )

        subtitle.setAlignment(Qt.AlignCenter)

        subtitle.setStyleSheet("""

        color:#94A3B8;

        font-size:15px;

        """)

        self.progress = QProgressBar()

        self.progress.setValue(0)

        self.loading = QLabel("Loading... 0%")

        self.loading.setAlignment(Qt.AlignCenter)

        self.loading.setStyleSheet("""

        color:#CBD5E1;

        font-size:13px;

        """)

        layout.addWidget(logo)
        layout.addSpacing(15)
        layout.addWidget(title)
        layout.addSpacing(8)
        layout.addWidget(subtitle)
        layout.addSpacing(30)
        layout.addWidget(self.progress)
        layout.addSpacing(10)
        layout.addWidget(self.loading)

        layout.addStretch()

        # ==========================
        # TIMER
        # ==========================

        self.timer = QTimer(self)

        self.timer.timeout.connect(
            self.update_progress
        )

        self.timer.start(25)
            # ==========================================
    # UPDATE PROGRESS
    # ==========================================

    def update_progress(self):

        value = self.progress.value()

        if value < 100:

            value += 1

            self.progress.setValue(value)

            self.loading.setText(
                f"Loading... {value}%"
            )

        else:

            self.timer.stop()

            self.open_login()

    # ==========================================
    # OPEN LOGIN WINDOW
    # ==========================================

    def open_login(self):

        try:

            self.login_window = LoginWindow()

            self.login_window.show()

            self.close()

        except Exception as e:

            from PySide6.QtWidgets import QMessageBox

            QMessageBox.critical(
                self,
                "Startup Error",
                str(e)
            )

            print("Splash Error :", e)