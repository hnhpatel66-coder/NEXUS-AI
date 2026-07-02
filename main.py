from database.database import create_database
import sys

from PySide6.QtWidgets import QApplication

from ui.splash.splash_screen import SplashScreen

create_database()

app = QApplication(sys.argv)

window = SplashScreen()

window.show()

sys.exit(app.exec())