from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import QTimer, Qt


class ThinkingWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.dots = 0

        self.label = QLabel("NEXUS AI is thinking")
        self.label.setAlignment(Qt.AlignCenter)

        self.label.setStyleSheet("""
            font-size:14px;
            color:#94A3B8;
            font-weight:bold;
        """)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

        # Timer for animation
        self.timer = QTimer()
        self.timer.timeout.connect(self.animate)

    # start animation
    def start(self):
        self.dots = 0
        self.timer.start(400)

    # stop animation
    def stop(self):
        self.timer.stop()
        self.label.setText("")

    # animation logic
    def animate(self):

        self.dots += 1

        if self.dots > 3:
            self.dots = 0

        self.label.setText(
            "NEXUS AI is thinking" + "." * self.dots
        )