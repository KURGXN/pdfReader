import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow, QWidget, QPushButton, QFileDialog, QVBoxLayout, QHBoxLayout

from PyQt6.QtPdfWidgets import QPdfView
from PyQt6.QtPdf import QPdfDocument

from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMaximumSize(950, 900)
        self.setMinimumSize(900, 850)
        self.setWindowTitle("PDF Reader")
        self.button = QPushButton("Загрузить", self)

        self.button.clicked.connect(self.load_file)

    def load_file(self, file_name=None, file_type=None):
        if not file_name or not file_type:
            file_name, file_type = QFileDialog.getOpenFileName(self, "Выберите файл", filter="PDF File (*.pdf)")

        self.setWindowTitle(file_name)

        self.document = QPdfDocument(None)
        self.document.load(file_name)

        view = QPdfView(None)
        view.setPageMode(QPdfView.PageMode.SinglePage)  # Просмотр всего документа
        view.setDocument(self.document)
        view.setZoomMode(QPdfView.ZoomMode.FitInView)
        view.setFixedSize(870, 800)

        layout = QHBoxLayout()
        layout.addWidget(view)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
