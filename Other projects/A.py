import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QLineEdit, QPushButton, QVBoxLayout, QWidget
from pytube import YouTube


class Downloader(QWidget):

    def __init__(self):
        super().__init__()
        self.line_edit = QLineEdit()
        self.button = QPushButton("Download")
        self.button.clicked.connect(self.download)
        layout = QVBoxLayout()
        layout.addWidget(self.line_edit)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def download(self):
        url = self.line_edit.text()
        yt = YouTube(url)
        video = yt.streams.first()
        video.download()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    downloader = Downloader()
    downloader.show()
    sys.exit(app.exec_())
