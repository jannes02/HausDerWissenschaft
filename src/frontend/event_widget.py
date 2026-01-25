from PySide6.QtCore import QFile
from PySide6.QtWidgets import QWidget, QVBoxLayout, QComboBox, QLineEdit, QTextEdit

from rsc_path import rsc_path
from src.backend.event_description import EventDescription
from src.frontend.advancedqcombobox import AdvancedQComboBox
from src.frontend.custom_ui_loader import CustomUiLoader


class EventWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        loader = CustomUiLoader()
        file = QFile(rsc_path("ui/event_widget.ui"))
        file.open(QFile.ReadOnly)
        ui = loader.load(file, self)
        file.close()

        # Layout korrekt übernehmen
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(ui)

        ui.btn_remove.clicked.connect(lambda: parent.remove_widget(self))

        self.le_title = self.findChild(QLineEdit, "le_title")
        self.le_host = self.findChild(QLineEdit, "le_host")
        self.le_time = self.findChild(QLineEdit, "le_time")
        self.cb_location = self.findChild(AdvancedQComboBox, "cb_location")
        self.te_description = self.findChild(QTextEdit, "te_description")

        self.le_title.editingFinished.connect(parent.compile)
        self.le_host.editingFinished.connect(parent.compile)
        self.le_time.editingFinished.connect(parent.compile)
        self.cb_location.currentTextChanged.connect(parent.compile)
        self.te_description.textChanged.connect(parent.compile)




    def get_data(self):
        ed = EventDescription()
        ed.title = self.findChild(QLineEdit, "le_title").text()
        ed.host_name = self.findChild(QLineEdit, "le_host").text()
        ed.time = self.findChild(QLineEdit, "le_time").text()
        ed.location = self.findChild(AdvancedQComboBox, "cb_location").currentText()
        plain = self.findChild(QTextEdit, "te_description").toPlainText()
        plain = plain.replace("\n", "<br/>")
        ed.description = plain
        return ed

