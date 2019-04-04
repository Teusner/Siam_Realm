from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt


class Login(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)

        self.initGUI()
        self.setWindowTitle("Login")
        self.setStyleSheet("background-color: #2d3436; color: white; font-size: 18px;")
        self.setWindowIcon(QtGui.QIcon('./content/rock.png'))
        self.setFixedSize(380, 220)

    def initGUI(self):
        # Creating the title
        self.gTitle = QtWidgets.QLabel("King of Siam")
        self.gTitle.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.gTitle.setAlignment(Qt.AlignCenter)
        self.gTitle.setStyleSheet("font-weight: bold; font-size: 45px;")

        # Creating the elephant login
        self.eText = QtWidgets.QLabel("Elephant's name ")
        self.eName = QtWidgets.QLineEdit(self)
        self.eName.setStyleSheet("background-color: #b2bec3; color: #0984e3; font-weight: bold; font-size: 14px; padding: 4px; margin-left: 6px; border: 0px solid #aaa; border-radius: 0px;")

        # Creating the rhinoceros login
        self.rText = QtWidgets.QLabel("Rhinoceros name")
        self.rName = QtWidgets.QLineEdit(self)
        self.rName.setStyleSheet("background-color: #b2bec3; color: #d63031; font-weight: bold; font-size: 14px; padding: 4px; margin-left: 6px; margin-top: 6px; border: 0px solid #aaa; border-radius: 0px;")

        # Creating the login button
        self.buttonLogin = QtWidgets.QPushButton('Login', self)
        self.buttonLogin.clicked.connect(self.handleLogin)
        self.buttonLogin.setStyleSheet("height: 30px; font-size: 18px; color: white; margin-top: 6px; text-align: center; background: #2980b9; border: 0; border-bottom: 2px solid #2475ab;")

        eLayout = QtWidgets.QHBoxLayout()
        eLayout.addWidget(self.eText)
        eLayout.addWidget(self.eName)
        rLayout = QtWidgets.QHBoxLayout()
        rLayout.addWidget(self.rText)
        rLayout.addWidget(self.rName)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.gTitle)
        layout.addLayout(eLayout)
        layout.addLayout(rLayout)
        layout.addWidget(self.buttonLogin)

        self.setLayout(layout)


    def handleLogin(self):
        if self.eName.text() != '' and self.rName.text() != '':
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(
                self, 'Error', 'Enter usernames !')


class Game(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Game, self).__init__(parent)
        self.setFixedSize(600, 600)
        self.setWindowTitle("King of Siam")
        self.setStyleSheet("background-color: #2d3436; color: white; font-size: 18px;")
        self.setWindowIcon(QtGui.QIcon('./content/rock.png'))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            print("appui bouton gauche")
            print("position = " + str(event.x()) + " " + str(event.y()))


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = Login()

    eName, rName = login.eName.text(), login.rName.text()

    if login.exec_() == QtWidgets.QDialog.Accepted:
        gwin = Game()
        gwin.show()
        sys.exit(app.exec_())
