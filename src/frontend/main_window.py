import os
import sys

import PySide6
from PySide6 import QtCore
from PySide6.QtPdf import QPdfDocument
from PySide6.QtPdfWidgets import QPdfView
from PySide6.QtPrintSupport import QPrinter, QPrintPreviewDialog
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QScrollArea, QWidget, QSizePolicy, \
    QDialog
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Qt, QUrl

from src.backend.flyer_builder import FlyerBuilder
from src.frontend.event_widget import EventWidget

if hasattr(Qt, 'AA_EnableHighDpiScaling'):
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
if hasattr(Qt, 'AA_UseHighDpiPixmaps'):
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.event_widgets = []

        loader = QUiLoader()
        file = QFile("frontend/main_window.ui")
        file.open(QFile.ReadOnly)
        ui = loader.load(file)
        file.close()
        if not ui:
            print(loader.errorString())
            sys.exit(-1)

        self.setCentralWidget(ui.centralWidget())
        screen = QApplication.primaryScreen()
        geometry = screen.availableGeometry()
        print(int(geometry.width() * 0.6),
            int(geometry.height() * 0.6))
        self.resize(
            int(geometry.width() * 0.6),
            int(geometry.height() * 0.6)
        )

        self.pdf_widget = self.findChild(QWidget, "pdf_widget")
        self.doc = QPdfDocument(self)
        self.doc.load("HDW-Flyer.pdf")
        self.pdf_view = QPdfView(self)
        self.pdf_view.setDocument(self.doc)
        self.pdf_view.setZoomMode(QPdfView.ZoomMode.FitInView)
        self.pdf_view.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred))
        layout = QVBoxLayout(self.pdf_widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.pdf_view)

        self.btn_add_event = self.findChild(QPushButton, "btn_add_event")
        self.btn_compile = self.findChild(QPushButton, "btn_compile")
        ui.btn_print.clicked.connect(self.print_pdf)
        self.vbox_events = self.findChild(QVBoxLayout, "vb_events")

        self.btn_add_event.clicked.connect(self.add_widget)
        self.btn_compile.clicked.connect(self.compile)

    @QtCore.Slot()
    def add_widget(self):
        widget = EventWidget(self)
        self.event_widgets.append(widget)
        self.vbox_events.addWidget(widget)
        print(f"Added: {widget}")

    @QtCore.Slot()
    def remove_widget(self, widget):
        self.event_widgets.remove(widget)
        self.vbox_events.removeWidget(widget)
        widget.deleteLater()

    @QtCore.Slot()
    def compile(self):
        events = []
        for ew in self.event_widgets:
            events.append(ew.get_data())

        builder = FlyerBuilder("HDW-Flyer.pdf")
        builder.build(event_descriptions=events)
        self.refresh_pdf()

    @QtCore.Slot()
    def print_pdf(self):
        events = []
        for ew in self.event_widgets:
            events.append(ew.get_data())

        builder = FlyerBuilder("HDW-Flyer.pdf")
        builder.build(event_descriptions=events)
        self.refresh_pdf()
        self.print_pdf_dialog()

    def print_pdf_dialog(self):
        # Dein PDF-Pfad
        pdf_path = "HDW-Flyer.pdf"

        # Dialog mit PDF-Vorschau erstellen
        dialog = QDialog(self)
        dialog.setWindowTitle("PDF Drucken")
        dialog.resize(800, 600)

        layout = QVBoxLayout(dialog)

        # PDF anzeigen
        web_view = QWebEngineView()
        web_view.setUrl(QUrl.fromLocalFile(os.path.abspath(pdf_path)))
        layout.addWidget(web_view)

        # Druck-Button (öffnet den nativen Druckdialog)
        btn_print = QPushButton("Druckdialog öffnen")
        btn_print.clicked.connect(lambda: web_view.page().runJavaScript("window.print();"))
        layout.addWidget(btn_print)

        # Abbrechen-Button
        btn_close = QPushButton("Abbrechen")
        btn_close.clicked.connect(dialog.reject)
        layout.addWidget(btn_close)

        dialog.exec()

    def refresh_pdf(self):
        self.doc.load("HDW-Flyer.pdf")
        self.pdf_view.setDocument(self.doc)