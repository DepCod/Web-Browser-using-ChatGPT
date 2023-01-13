import sys
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtWidgets import QApplication, QLineEdit, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QToolBar


class Browser(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Deepak browser')

        # Create the widgets
        self.layout = QVBoxLayout()
        self.toolbar = QToolBar()
        self.view = QWebEngineView()

        # Set the URL to Google
        self.view.load(QUrl('https://www.google.com/'))

        # Add the buttons to the toolbar
        self.toolbar.addAction('Back', self.view.back)
        self.toolbar.addAction('Forward', self.view.forward)
        self.toolbar.addAction('Refresh', self.view.reload)

        # Add the view and toolbar to the layout
        self.layout.addWidget(self.toolbar)
        self.layout.addWidget(self.view)
        self.setLayout(self.layout)

app = QApplication(sys.argv)
browser = Browser()
browser.show()
app.exec_()
