import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QWidget

from rsc_path import rsc_path
from src.frontend.main_window import MainWindow

if __name__ == "__main__":

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(rsc_path("icons/app.ico")))
    app.setApplicationName("Haus Der Wissenschaft - Flyer Creator")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
