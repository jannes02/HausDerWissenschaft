import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

from src.frontend.event_widget import EventWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        file = QFile("frontend/main_window.ui")
        file.open(QFile.ReadOnly)
        ui = loader.load(file)
        file.close()
        if not ui:
            print(loader.errorString())
            sys.exit(-1)

        self.setCentralWidget(ui.centralWidget())
        self.resize(ui.size())

        self.btn_add_event = self.findChild(QPushButton, "btn_add_event")
        self.vbox_events = self.findChild(QVBoxLayout, "vbox_events")

        self.btn_add_event.clicked.connect(self.add_widget)

    def add_widget(self):
        widget = EventWidget()
        self.vbox_events.addWidget(widget)
        print(f"Added: {widget}")
