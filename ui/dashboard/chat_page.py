from services.ai_service import AIService

from ui.widgets.message_widget import MessageWidget
from ui.widgets.code_block import CodeBlock

from ui.chat.chat_parser import ChatParser
from ui.chat.markdown_renderer import MarkdownRenderer
from ui.chat.stream_writer import StreamWriter
from ui.chat.thinking_widget import ThinkingWidget

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QVBoxLayout,
    QHBoxLayout,
    QScrollArea,
    QFrame,
)

from PySide6.QtCore import Qt


class ChatPage(QWidget):

    def __init__(self):
        super().__init__()

        self.setObjectName("ChatPage")

        # ======================================
        # STYLE
        # ======================================

        self.setStyleSheet("""

        QWidget#ChatPage{

            background:#0F172A;
        }

        QLabel{

            color:white;
            font-family:Segoe UI;
        }

        QScrollArea{

            border:none;
            background:#0F172A;
        }

        QScrollArea QWidget{

            background:#0F172A;
        }

        QLineEdit{

            background:#111827;
            border:1px solid #334155;
            border-radius:14px;

            padding:12px;

            color:white;

            font-size:14px;
        }

        QPushButton{

            background:#2563EB;

            color:white;

            border:none;

            border-radius:12px;

            padding:12px 18px;

            font-size:14px;

            font-weight:bold;
        }

        QPushButton:hover{

            background:#1D4ED8;
        }

        """)

        # ======================================
        # MAIN LAYOUT
        # ======================================

        self.main_layout = QVBoxLayout(self)

        self.main_layout.setContentsMargins(
            20,
            20,
            20,
            20
        )

        self.main_layout.setSpacing(15)

        # ======================================
        # HEADER
        # ======================================

        header = QHBoxLayout()

        self.title = QLabel("💬 NEXUS AI")

        self.title.setStyleSheet("""

            font-size:28px;

            font-weight:bold;

            color:#60A5FA;

        """)

        self.status = QLabel("🟢 Online")

        self.status.setStyleSheet("""

            color:#22C55E;

            font-size:14px;

            font-weight:bold;

        """)

        header.addWidget(self.title)

        header.addStretch()

        header.addWidget(self.status)

        self.main_layout.addLayout(header)

        # ======================================
        # CHAT AREA
        # ======================================

        self.scroll = QScrollArea()

        self.scroll.setWidgetResizable(True)

        self.chat_container = QWidget()

        self.chat_layout = QVBoxLayout()

        self.chat_layout.setSpacing(12)

        self.chat_layout.addStretch()

        self.chat_container.setLayout(
            self.chat_layout
        )

        self.scroll.setWidget(
            self.chat_container
        )

        self.main_layout.addWidget(
            self.scroll
        )
                # ======================================
        # INPUT AREA (ChatGPT Style)
        # ======================================

        bottom = QHBoxLayout()
        bottom.setSpacing(10)

        input_frame = QFrame()

        input_frame.setStyleSheet("""
        QFrame{

            background:#111827;

            border:1px solid #334155;

            border-radius:18px;

        }
        """)

        input_layout = QHBoxLayout(input_frame)

        input_layout.setContentsMargins(
            12,
            6,
            8,
            6
        )

        # ======================================
        # MESSAGE INPUT
        # ======================================

        self.message_input = QLineEdit()

        self.message_input.setPlaceholderText(
            "Message NEXUS AI..."
        )

        self.message_input.setStyleSheet("""
        QLineEdit{

            border:none;

            background:transparent;

            color:white;

            font-size:14px;

            padding:8px;

        }
        """)

        # ======================================
        # SEND BUTTON
        # ======================================

        self.send_button = QPushButton("➤")

        self.send_button.setFixedSize(46,46)

        self.send_button.setCursor(
            Qt.PointingHandCursor
        )

        self.send_button.setStyleSheet("""

        QPushButton{

            background:#2563EB;

            border:none;

            border-radius:23px;

            font-size:18px;

            font-weight:bold;

        }

        QPushButton:hover{

            background:#1D4ED8;

        }

        """)

        input_layout.addWidget(self.message_input)
        input_layout.addWidget(self.send_button)

        bottom.addWidget(input_frame)

        self.main_layout.addLayout(bottom)

        # ======================================
        # SYSTEM VARIABLES
        # ======================================

        self.current_ai_widget = None

        self.stream_writer = StreamWriter(
            self.update_stream
        )

        self.thinking_widget = ThinkingWidget()

        # ======================================
        # WELCOME MESSAGE
        # ======================================

        self.add_message(
            "ai",
            "Hello 👋\n\nI am NEXUS AI.\nHow can I help you today?"
        )

        # ======================================
        # EVENTS
        # ======================================

        self.send_button.clicked.connect(
            self.send_message
        )

        self.message_input.returnPressed.connect(
            self.send_message
        )
            # ==========================================================
    # ADD WIDGET
    # ==========================================================

    def add_widget(self, widget):

        # Stretch પહેલાં widget add કરો
        self.chat_layout.insertWidget(
            self.chat_layout.count() - 1,
            widget
        )

        # Auto Scroll
        scrollbar = self.scroll.verticalScrollBar()
        scrollbar.setValue(
            scrollbar.maximum()
        )

    # ==========================================================
    # ADD MESSAGE
    # ==========================================================

    def add_message(self, sender, message):

        widget = MessageWidget(
            sender,
            message
        )

        self.add_widget(widget)

    # ==========================================================
    # ADD CODE BLOCK
    # ==========================================================

    def add_code(self, language, code):

        widget = CodeBlock(
            language,
            code
        )

        self.add_widget(widget)

    # ==========================================================
    # UPDATE STREAM
    # ==========================================================

    def update_stream(self, text):

        if self.current_ai_widget:

            html = MarkdownRenderer.render(text)

            self.current_ai_widget.set_message(
                html
            )

        # Auto Scroll while streaming
        scrollbar = self.scroll.verticalScrollBar()

        scrollbar.setValue(
            scrollbar.maximum()
        )
            # ==========================================================
    # SEND MESSAGE
    # ==========================================================

    def send_message(self):

        message = self.message_input.text().strip()

        if not message:
            return

        # ======================================
        # USER MESSAGE
        # ======================================

        self.add_message(
            "user",
            message
        )

        self.message_input.clear()

        # ======================================
        # SHOW THINKING
        # ======================================

        self.add_widget(
            self.thinking_widget
        )

        self.thinking_widget.start()

        # Disable input while AI replying
        self.message_input.setEnabled(False)
        self.send_button.setEnabled(False)

        # ======================================
        # GET AI RESPONSE
        # ======================================

        try:

            reply = AIService.ask_ai(message)

        except Exception as e:

            self.thinking_widget.stop()

            self.add_message(
                "ai",
                f"❌ Error\n\n{str(e)}"
            )

            self.message_input.setEnabled(True)
            self.send_button.setEnabled(True)

            return

        # ======================================
        # REMOVE THINKING
        # ======================================

        self.chat_layout.removeWidget(
            self.thinking_widget
        )

        self.thinking_widget.deleteLater()

        self.thinking_widget = ThinkingWidget()

        # ======================================
        # PARSE RESPONSE
        # ======================================

        blocks = ChatParser.parse(reply)

        # ======================================
        # SHOW BLOCKS
        # ======================================

        for block in blocks:

            if block["type"] == "text":

                self.current_ai_widget = MessageWidget(
                    "ai",
                    ""
                )

                self.add_widget(
                    self.current_ai_widget
                )

                self.stream_writer.start(
                    block["content"]
                )

            elif block["type"] == "code":

                self.add_code(
                    block["language"],
                    block["content"]
                )

        # ======================================
        # ENABLE INPUT AGAIN
        # ======================================

        self.message_input.setEnabled(True)
        self.send_button.setEnabled(True)

        self.message_input.setFocus()

        # ======================================
        # AUTO SCROLL
        # ======================================

        scrollbar = self.scroll.verticalScrollBar()

        scrollbar.setValue(
            scrollbar.maximum()
        )