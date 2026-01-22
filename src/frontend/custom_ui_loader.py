from PySide6.QtUiTools import QUiLoader

from src.frontend.advancedqcombobox import AdvancedQComboBox


class CustomUiLoader(QUiLoader):
    """Customizes the QUiLoader Class to load custom Widgets"""
    def createWidget(self, className, parent=None, name=""):
        if className == "AdvancedQComboBox":
            widget = AdvancedQComboBox(parent)
            widget.setObjectName(name)
            return widget
        # Alle anderen Widgets werden standardmäßig erstellt
        return super().createWidget(className, parent, name)