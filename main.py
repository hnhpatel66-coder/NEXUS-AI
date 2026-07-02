from database.database import create_database
import sys

from PySide6.QtWidgets import QApplication

from ui.login.register_window import RegisterWindow

create_database()

app = QApplication(sys.argv)

window = RegisterWindow()

window.show()

sys.exit(app.exec())