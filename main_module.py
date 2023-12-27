from PyQt6.QtWidgets import QMainWindow, QWidget, QPushButton, QFileDialog, QVBoxLayout, QHBoxLayout

from PyQt6.QtPdfWidgets import QPdfView
from PyQt6.QtPdf import QPdfDocument


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(950, 900)
        self.setWindowTitle("PDF Reader")
        """ Установка размера окна и его названия """

        self.layout = QVBoxLayout()
        """ Основной макет """
        
        self.load_button()
        # self.previous_button()
        # self.next_button()

    def load_button(self):
        button = QPushButton("Загрузить", self)
        button.setFixedSize(80, 30)
        button.move(10, 10)
        self.layout.addWidget(button)
        button.clicked.connect(self.load_file)

    def load_file(self):
        file_name, file_type = QFileDialog.getOpenFileName(self, "Выберите файл", filter="PDF File (*.pdf)")

        if not file_name:
            return

        self.setWindowTitle(file_name)

        self.document = QPdfDocument(None)
        self.document.load(file_name)

        view = QPdfView(None)
        view.setPageMode(QPdfView.PageMode.MultiPage)
        view.setDocument(self.document)
        view.setZoomMode(QPdfView.ZoomMode.FitInView)
        view.setFixedSize(870, 800)

        self.layout.addWidget(view)

        widget = QWidget()
        widget.setLayout(self.layout)

        self.setCentralWidget(widget)

    # def previous_button(self):
    #     button = QPushButton("<", self)
    #     button.setFixedSize(60, 30)
    #     button.move(810, 10)
    #     self.layout.addWidget(button)
    #     button.clicked.connect(self.previous_page)
    #
    # def previous_page(self):
    #     pass
    #
    # def next_button(self):
    #     button = QPushButton(">", self)
    #     button.setFixedSize(60, 30)
    #     button.move(880, 10)
    #     self.layout.addWidget(button)
    #     button.clicked.connect(self.previous_page)
    #
    # def next_page(self):
    #     pass
