from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QWidget, QVBoxLayout


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
