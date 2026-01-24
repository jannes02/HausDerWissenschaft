import sys

from PySide6.QtWidgets import QApplication, QWidget

from src.backend.event_description import EventDescription
from src.backend.flyer_builder import FlyerBuilder
from src.frontend.main_window import MainWindow

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
