from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
import sys
import main


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        # self.qbtn = QtWidgets.QPushButton(self)
        self.grid = QGridLayout()
        self.submit = QtWidgets.QPushButton(self)
        self.newMovie = QtWidgets.QPushButton(self)
        self.movieTitle = QtWidgets.QTextEdit(self)
        self.genreCheck = QtWidgets.QCheckBox(self)
        self.actorCheck = QtWidgets.QCheckBox(self)
        self.yearCheck = QtWidgets.QCheckBox(self)
        self.genreText = QtWidgets.QComboBox(self)
        self.actorText = QtWidgets.QLineEdit(self)
        self.yearText = QtWidgets.QLineEdit(self)

        self.init_ui()

    def init_ui(self):
        app = QApplication(sys.argv)
        self.setWindowTitle("Movie Picker")
        font = QtGui.QFont()
        font.setPointSize(18)

        # self.qbtn.setText("X")
        # self.qbtn.clicked.connect(QApplication.instance().quit)
        # self.qbtn.resize(self.qbtn.sizeHint())
        # self.qbtn.move(10, 10)

        self.movieTitle.setFont(font)
        self.movieTitle.move(500, 200)

        self.genreCheck.setFont(font)
        self.genreCheck.setText("Genre")

        self.genreText.addItems(main.get_genres().keys())

        self.actorCheck.setFont(font)
        self.actorCheck.setText("Actor/Actress")

        self.actorText.setFont(font)

        self.yearCheck.setFont(font)
        self.yearCheck.setText("Year")

        self.yearText.setFont(font)

        self.submit.setText("Submit")
        self.submit.resize(QtCore.QSize(40, 40))
        self.submit.clicked.connect(self.on_submit)

        self.newMovie.setText("Amanda says NO")
        self.newMovie.move(500, 300)
        self.newMovie.clicked.connect(self.on_click)

        self.grid.setSpacing(10)
        self.grid.setRowStretch(0, 1)
        self.grid.addWidget(self.genreCheck, 1, 0, 1, 3)
        self.grid.addWidget(self.genreText, 2, 0, 1, 3)
        self.grid.addWidget(self.actorCheck, 3, 0, 1, 3)
        self.grid.addWidget(self.actorText, 4, 0, 1, 3)
        self.grid.addWidget(self.yearCheck, 5, 0, 1, 3)
        self.grid.addWidget(self.yearText, 6, 0, 1, 3)
        self.grid.setRowStretch(7, 1)
        self.grid.addWidget(self.submit, 8, 1, 1, 1)
        self.grid.addWidget(self.newMovie, 8, 1, 1, 1)
        self.grid.setRowStretch(9, 1)
        print(self.grid.rowCount())
        print(self.grid.columnCount())
        self.setLayout(self.grid)

        self.setGeometry(200, 200, 500, 300)
        self.main_ui()
        sys.exit(app.exec_())

    def main_ui(self):
        self.genreCheck.setEnabled(True)
        self.genreCheck.setVisible(True)

        self.genreText.setEnabled(True)
        self.genreText.setVisible(True)

        self.actorCheck.setEnabled(True)
        self.actorCheck.setVisible(True)

        self.actorText.setEnabled(True)
        self.actorText.setVisible(True)

        self.yearCheck.setEnabled(True)
        self.yearCheck.setVisible(True)

        self.yearText.setEnabled(True)
        self.yearText.setVisible(True)

        self.submit.setEnabled(True)
        self.submit.setVisible(True)

        self.movieTitle.setEnabled(False)
        self.movieTitle.setEnabled(False)

        self.newMovie.setEnabled(False)
        self.newMovie.setVisible(False)

        self.show()

    def movie_ui(self, movie):
        self.genreCheck.setEnabled(False)
        self.genreCheck.setVisible(False)

        self.genreText.setEnabled(False)
        self.genreText.setVisible(False)

        self.actorCheck.setEnabled(False)
        self.actorCheck.setVisible(False)

        self.actorText.setEnabled(False)
        self.actorText.setVisible(False)

        self.yearCheck.setEnabled(False)
        self.yearCheck.setVisible(False)

        self.yearText.setEnabled(False)
        self.yearText.setVisible(False)

        self.submit.setEnabled(False)
        self.submit.setVisible(False)

        self.movieTitle.setEnabled(True)
        self.movieTitle.setEnabled(True)

        #figure out text update
        self.movieTitle.setText(movie['title'])
        self.movieTitle.update()

        self.newMovie.setEnabled(True)
        self.newMovie.setVisible(True)

        self.show()

    def on_submit(self):
        if self.genreCheck.isTristate():
            genre = self.genreText.currentText()
        else:
            genre = ""

        if self.actorCheck.isTristate():
            actor = self.actorText.text()
        else:
            actor = ""

        if self.yearCheck.isTristate():
            year = self.yearText.text()
        else:
            year = ""

        discover, add_ons = main.get_addons(genre, actor, year)
        print(discover, add_ons)
        movie = main.get_movie(discover, add_ons)
        print(movie['title'],":",movie['overview'])
        self.movie_ui(movie)

    def on_click(self):
        # main.main()
        self.main_ui()


def window():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
