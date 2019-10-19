import sys
from PySide2.QtWidgets import (QApplication, QLabel, QPushButton,
                               QVBoxLayout, QWidget, QLineEdit, QListWidget)
from PySide2.QtCore import Slot, Qt
from endings import find_similar_ending_words

class MyWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)


        self.search = QLineEdit()

        self.results = QListWidget()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.search)
        self.layout.addWidget(self.results)
        self.setLayout(self.layout)

        self.search.returnPressed.connect(self.search_word)

    @Slot()
    def search_word(self):
        self.results.clear()
        for word in find_similar_ending_words(self.search.text()):
            self.results.addItem(word)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())
