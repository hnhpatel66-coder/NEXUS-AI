from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QHBoxLayout,
)

from PySide6.QtCore import (
    Qt,
    QTimer,
)


class ThinkingWidget(QWidget):
    """
    ChatGPT Style Thinking Animation
    """

    def __init__(self):
        super().__init__()

        self.dots = 0

        self.setStyleSheet("""
            QWidget{
                background:transparent;
            }

            QLabel{
                color:#94A3B8;
                font-size:14px;
                font-family:'Segoe UI';
                padding:10px;
            }
        """)

        layout = QHBoxLayout(self)

        layout.setContentsMargins(
            15,
            10,
            15,
            10
        )

        layout.setAlignment(Qt.AlignLeft)

        self.label = QLabel()

        layout.addWidget(self.label)

        self.timer = QTimer(self)

        self.timer.timeout.connect(
            self.animate
        )

        self.stop()

    # =====================================
    # START
    # =====================================

    def start(self):

        self.dots = 0

        self.show()

        self.timer.start(400)

    # =====================================
    # STOP
    # =====================================

    def stop(self):

        self.timer.stop()

        self.label.setText("")

        self.hide()

    # =====================================
    # ANIMATION
    # =====================================

    def animate(self):

        self.dots += 1

        if self.dots > 3:
            self.dots = 0

        self.label.setText(
            "🤖 NEXUS AI is thinking" + "." * self.dots
        )

    # =====================================
    # CHANGE TEXT
    # =====================================

    def set_text(self, text: str):

        self.label.setText(text)

    # =====================================
    # IS RUNNING
    # =====================================

    def is_running(self):

        return self.timer.isActive()