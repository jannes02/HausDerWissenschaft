from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QWidget, QVBoxLayout, QComboBox, QLineEdit, QTextEdit

from src.backend.event_description import EventDescription


class EventWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        loader = QUiLoader()
        file = QFile("frontend/event_widget.ui")
        file.open(QFile.ReadOnly)
        ui = loader.load(file, self)
        file.close()

        # Layout korrekt übernehmen
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(ui)

        self.findChild(QComboBox, "cb_location").addItems(["Sitzungsraum DG", "Beispielraum"]) #todo: add rooms to json when saving

    def get_data(self):
        ed = EventDescription()
        ed.title = self.findChild(QLineEdit, "le_title").text()
        ed.host_name = self.findChild(QLineEdit, "le_host").text()
        ed.time = self.findChild(QLineEdit, "le_time").text()
        ed.location = self.findChild(QComboBox, "cb_location").currentText()
        plain = self.findChild(QTextEdit, "te_description").toPlainText()
        plain = plain.replace("\n", "<br/>")
        ed.description = plain
        return ed

