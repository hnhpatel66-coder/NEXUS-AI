from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QLabel,
    QScrollArea,
    QFrame,
)

from PySide6.QtCore import (
    Qt,
    QThread,
    Signal,
)

from PySide6.QtGui import QCursor

from ui.widgets.message_widget import MessageWidget
from ui.widgets.code_block import CodeBlock
from ui.chat.thinking_widget import ThinkingWidget
from ui.chat.stream_writer import StreamWriter
from ui.chat.chat_parser import ChatParser
from ui.chat.markdown_renderer import MarkdownRenderer

from services.ai_service import AIService


# ==========================================================
# AI Worker Thread
# ==========================================================

class AIWorker(QThread):

    finished = Signal(str)
    failed = Signal(str)

    def __init__(self, prompt):
        super().__init__()

        self.prompt = prompt

    def run(self):

        try:

            response = AIService.generate_response(
                self.prompt
            )

            self.finished.emit(response)

        except Exception as e:

            self.failed.emit(str(e))


# ==========================================================
# CHAT PAGE
# ==========================================================

class ChatPage(QWidget):

    def __init__(self):
        super().__init__()

        self.worker = None

        self.current_ai_widget = None

        self.stream_writer = None

        self.setup_ui()

        # ==========================================================
    # UI
    # ==========================================================

    def setup_ui(self):

        self.setStyleSheet("""
        QWidget{
            background:#0F172A;
            color:white;
            font-family:'Segoe UI';
        }

        QLineEdit{
            background:#111827;
            border:1px solid #334155;
            border-radius:18px;
            padding:14px;
            color:white;
            font-size:14px;
        }

        QLineEdit:focus{
            border:2px solid #2563EB;
        }

        QPushButton{
            background:#2563EB;
            color:white;
            border:none;
            border-radius:18px;
            font-size:15px;
            font-weight:bold;
            padding:12px;
        }

        QPushButton:hover{
            background:#1D4ED8;
        }

        QScrollArea{
            border:none;
            background:transparent;
        }
        """)

        main_layout = QVBoxLayout(self)

        main_layout.setContentsMargins(
            18,
            18,
            18,
            18
        )

        main_layout.setSpacing(12)

        # =====================================
        # TITLE
        # =====================================

        title = QLabel("💬 NEXUS AI")

        title.setStyleSheet("""
            font-size:24px;
            font-weight:bold;
            color:#60A5FA;
        """)

        main_layout.addWidget(title)

        # =====================================
        # SCROLL AREA
        # =====================================

        self.scroll = QScrollArea()

        self.scroll.setWidgetResizable(True)

        self.scroll.setHorizontalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff
        )

        self.chat_container = QWidget()

        self.chat_layout = QVBoxLayout(
            self.chat_container
        )

        self.chat_layout.setSpacing(14)

        self.chat_layout.setContentsMargins(
            0,
            0,
            0,
            0
        )

        self.chat_layout.addStretch()

        self.scroll.setWidget(
            self.chat_container
        )

        main_layout.addWidget(self.scroll)

        # =====================================
        # INPUT BAR
        # =====================================

        bottom = QHBoxLayout()

        self.input = QLineEdit()

        self.input.setPlaceholderText(
            "Message NEXUS AI..."
        )

        self.input.returnPressed.connect(
            self.send_message
        )

        bottom.addWidget(self.input)

        self.send_btn = QPushButton("➤")

        self.send_btn.setFixedSize(55,55)

        self.send_btn.setCursor(
            QCursor(Qt.PointingHandCursor)
        )

        self.send_btn.clicked.connect(
            self.send_message
        )

        bottom.addWidget(
            self.send_btn
        )

        main_layout.addLayout(bottom)

        # =====================================
        # THINKING
        # =====================================

        self.thinking = ThinkingWidget()

        self.thinking.hide()

        self.chat_layout.insertWidget(
            self.chat_layout.count()-1,
            self.thinking
        )

        # =====================================
        # STREAM WRITER
        # =====================================

        self.stream_writer = StreamWriter(
            self.stream_update
        )

        self.stream_writer.finished.connect(
            self.stream_finished
        )

        # =====================================
        # WELCOME MESSAGE
        # =====================================

        welcome = MessageWidget(
            "ai",
            MarkdownRenderer.render(
                "# 👋 Welcome\n\nI am **NEXUS AI**.\n\nHow can I help you today?"
            )
        )

        self.add_widget(welcome)
            # ==========================================================
    # SEND MESSAGE
    # ==========================================================

    def send_message(self):

        prompt = self.input.text().strip()

        if not prompt:
            return

        # User Message
        user_widget = MessageWidget(
            "user",
            MarkdownRenderer.render(prompt)
        )

        self.add_widget(user_widget)

        self.input.clear()

        self.input.setEnabled(False)

        self.send_btn.setEnabled(False)

        # Thinking Animation
        self.thinking.start()

        self.auto_scroll()

        # AI Thread
        self.worker = AIWorker(prompt)

        self.worker.finished.connect(
            self.receive_ai_response
        )

        self.worker.failed.connect(
            self.receive_error
        )

        self.worker.start()

    # ==========================================================
    # RECEIVE RESPONSE
    # ==========================================================

    def receive_ai_response(self, response):

        self.thinking.stop()

        self.current_ai_widget = MessageWidget(
            "ai",
            ""
        )

        self.add_widget(
            self.current_ai_widget
        )

        self.stream_writer.start(response)

    # ==========================================================
    # RECEIVE ERROR
    # ==========================================================

    def receive_error(self, error):

        self.thinking.stop()

        widget = MessageWidget(
            "ai",
            f"<b>❌ Error</b><br><br>{error}"
        )

        self.add_widget(widget)

        self.input.setEnabled(True)

        self.send_btn.setEnabled(True)

        self.input.setFocus()

        # ==========================================================
    # STREAM UPDATE
    # ==========================================================

    def stream_update(self, text):

        if self.current_ai_widget is None:
            return

        html = MarkdownRenderer.render(text)

        self.current_ai_widget.set_message(html)

        self.auto_scroll()

    # ==========================================================
    # STREAM FINISHED
    # ==========================================================

    def stream_finished(self):

        if self.current_ai_widget is None:

            self.input.setEnabled(True)

            self.send_btn.setEnabled(True)

            self.input.setFocus()

            return

        response = self.stream_writer.text

        blocks = ChatParser.parse(response)

        if len(blocks) > 1:

            self.chat_layout.removeWidget(
                self.current_ai_widget
            )

            self.current_ai_widget.deleteLater()

            self.current_ai_widget = None

            for block in blocks:

                if block["type"] == "text":

                    widget = MessageWidget(
                        "ai",
                        MarkdownRenderer.render(
                            block["content"]
                        )
                    )

                    self.add_widget(widget)

                elif block["type"] == "code":

                    widget = CodeBlock(
                        block["language"],
                        block["content"]
                    )

                    self.add_widget(widget)

        self.input.setEnabled(True)

        self.send_btn.setEnabled(True)

        self.input.setFocus()

        self.auto_scroll()
            # ==========================================================
    # ADD WIDGET
    # ==========================================================

    def add_widget(self, widget):

        self.chat_layout.insertWidget(
            self.chat_layout.count() - 1,
            widget
        )

        self.auto_scroll()

    # ==========================================================
    # AUTO SCROLL
    # ==========================================================

    def auto_scroll(self):

        scrollbar = self.scroll.verticalScrollBar()

        scrollbar.setValue(
            scrollbar.maximum()
        )

    # ==========================================================
    # CLEAR CHAT
    # ==========================================================

    def clear_chat(self):

        while self.chat_layout.count() > 1:

            item = self.chat_layout.takeAt(0)

            if item.widget():

                item.widget().deleteLater()

        self.current_ai_widget = None

    # ==========================================================
    # ADD USER MESSAGE
    # ==========================================================

    def add_user_message(self, text):

        widget = MessageWidget(
            "user",
            MarkdownRenderer.render(text)
        )

        self.add_widget(widget)

    # ==========================================================
    # ADD AI MESSAGE
    # ==========================================================

    def add_ai_message(self, text):

        widget = MessageWidget(
            "ai",
            MarkdownRenderer.render(text)
        )

        self.add_widget(widget)

    # ==========================================================
    # ADD SYSTEM MESSAGE
    # ==========================================================

    def add_system_message(self, text):

        widget = MessageWidget(
            "ai",
            f"""
            <div style="
                background:#1E293B;
                border-left:4px solid #3B82F6;
                padding:12px;
                border-radius:10px;
            ">
            {MarkdownRenderer.render(text)}
            </div>
            """
        )

        self.add_widget(widget)

    # ==========================================================
    # SET INPUT ENABLED
    # ==========================================================

    def set_input_enabled(self, enabled: bool):

        self.input.setEnabled(enabled)

        self.send_btn.setEnabled(enabled)

    # ==========================================================
    # FOCUS INPUT
    # ==========================================================

    def focus_input(self):

        self.input.setFocus()

    # ==========================================================
    # CLOSE EVENT
    # ==========================================================

    def closeEvent(self, event):

        try:

            if self.worker and self.worker.isRunning():

                self.worker.quit()

                self.worker.wait()

        except Exception:

            pass

        event.accept()