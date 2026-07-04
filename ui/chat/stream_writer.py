from PySide6.QtCore import QTimer


class StreamWriter:

    def __init__(self, callback):
        self.callback = callback

        self.text = ""
        self.index = 0
        self.timer = QTimer()

        self.timer.timeout.connect(self.write_next)

    # =========================
    # START STREAM
    # =========================
    def start(self, text: str):

        self.text = text
        self.index = 0

        self.timer.start(15)  # speed (lower = faster)

    # =========================
    # WRITE CHARACTER BY CHARACTER
    # =========================
    def write_next(self):

        if self.index < len(self.text):

            self.index += 1

            current_text = self.text[:self.index]

            self.callback(current_text)

        else:
            self.timer.stop()