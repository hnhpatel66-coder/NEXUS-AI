from PySide6.QtCore import QObject, QTimer, Signal


class StreamWriter(QObject):
    """
    ChatGPT Style Streaming Writer
    Streams text character-by-character.
    """

    updated = Signal(str)
    finished = Signal()

    def __init__(self, callback=None, interval=15):
        super().__init__()

        self.callback = callback
        self.interval = interval

        self._text = ""
        self._index = 0
        self._streaming = False

        self.timer = QTimer(self)
        self.timer.timeout.connect(self._write_next)

    # ==========================================
    # Start Streaming
    # ==========================================

    def start(self, text: str):

        self.stop()

        self._text = text or ""
        self._index = 0
        self._streaming = True

        self.timer.start(self.interval)

    # ==========================================
    # Internal Writer
    # ==========================================

    def _write_next(self):

        if self._index >= len(self._text):

            self.stop()

            self.finished.emit()

            return

        self._index += 1

        current = self._text[:self._index]

        if self.callback:
            self.callback(current)

        self.updated.emit(current)

    # ==========================================
    # Stop Streaming
    # ==========================================

    def stop(self):

        if self.timer.isActive():
            self.timer.stop()

        self._streaming = False

    # ==========================================
    # Finish Immediately
    # ==========================================

    def finish(self):

        self.stop()

        if self.callback:
            self.callback(self._text)

        self.updated.emit(self._text)

        self.finished.emit()

    # ==========================================
    # Clear
    # ==========================================

    def clear(self):

        self.stop()

        self._text = ""
        self._index = 0

    # ==========================================
    # Speed
    # ==========================================

    def set_interval(self, interval: int):

        self.interval = max(1, interval)

        if self.timer.isActive():

            self.timer.start(self.interval)

    # ==========================================
    # Getters
    # ==========================================

    @property
    def text(self):
        return self._text

    @property
    def streaming(self):
        return self._streaming

    @property
    def progress(self):

        if not self._text:
            return 0

        return int((self._index / len(self._text)) * 100)