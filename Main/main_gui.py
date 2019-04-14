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
        self.buttonLogin.setStyleSheet("height: 30px; font-size: 18px; color: white; margin-top: 6px; text-align: center; background: #2980b9; border: 0; border-bottom: 2px solid #2475ab; border-right: 2px solid #2475ab;")

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


class Game(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Game, self).__init__(parent)
        self.setFixedSize(370, 415)
        self.setWindowTitle("King of Siam")
        self.setStyleSheet("background-color: #2d3436; color: white; font-size: 18px;")
        self.setWindowIcon(QtGui.QIcon('./content/rock.png'))

        # Showing the gamemap
        label = QtWidgets.QLabel(self)
        Pixmap = QtGui.QPixmap('./content/gamemap.png')
        label.setPixmap(Pixmap)
        label.setGeometry(10, 5, 360, 360)

        # Creating the coordinates of the tiles
        xcoords, ycoords = [15, 84, 153, 222, 291], [15, 84, 153, 222, 291]
        self.coord = [[(x, y) for x in xcoords] for y in ycoords]

        self.tile = []
        for j in range(5):
            l=[]
            for i in range(5):
                label = QtWidgets.QLabel(self)
                #Pixmap = QtGui.QPixmap('./content/rhinoceros.png')
                #label.setPixmap(Pixmap)
                label.setStyleSheet("background-color: rgba(0, 0, 0, 0%);")
                x, y = self.coord[i][j]
                label.setGeometry(x, y, 64, 64)
                l.append(label)
            self.tile.append(l)


        layout = QtWidgets.QVBoxLayout(self)

        # Creating the buttons
        self.buttonCancel = QtWidgets.QPushButton('Cancel', self)
        self.buttonCancel.setStyleSheet("height: 30px; font-size: 18px; color: white; margin-top: 6px; text-align: center; background: #e74c3c; border: 0; border-bottom: 2px solid #c0392b; border-right: 2px solid #c0392b;")
        self.buttonCancel.setGeometry(15, 365, 165, 40)

        self.buttonValid = QtWidgets.QPushButton('Accept', self)
        self.buttonValid.setStyleSheet("height: 30px; font-size: 18px; color: white; margin-top: 6px; text-align: center; background: #2ecc71; border: 0; border-bottom: 2px solid #27ae60; border-right: 2px solid #27ae60;")
        self.buttonValid.setGeometry(190, 365, 165, 40)

        layoutButtons = QtWidgets.QHBoxLayout()
        layoutButtons.addWidget(self.buttonCancel)
        layoutButtons.addWidget(self.buttonValid)

        #layout.addLayout(layoutButtons)

        self.setLayout(layout)


        self.show()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            seli, selj = int((event.x()-10)/66.5), int((event.y()-15)/66.5)

            print("appui bouton gauche")
            print("position = " + str(seli) + " " + str(selj))
            for j in range(5):
                for i in range(5):
                    self.tile[i][j].setStyleSheet("background-color: rgba(0, 0, 0, 0%);")

            li = [-1, 0, 1]
            l = [(seli+x, selj+y) for x in li for y in li if seli+x>=0 and seli+x<5 and selj+y>=0 and selj+y<5 and abs(x*y) != 1]
            for k in l:
                m,n = k
                self.tile[m][n].setStyleSheet("background-color: #2ecc71")

            self.tile[seli][selj].setStyleSheet("background-color: #16a085")


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    """login = Login()

    eName, rName = login.eName.text(), login.rName.text()

    if login.exec_() == QtWidgets.QDialog.Accepted:"""
    gwin = Game()
    gwin.show()
    sys.exit(app.exec_())
