from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt

from Module.KingOfSiam import *
import numpy as np


class Login(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)

        self.initGUI()
        self.setWindowTitle("Login")
        self.setStyleSheet("background-color: #2d3436; color: white; font-size: 18px;")
        self.setWindowIcon(QtGui.QIcon('./content/boulder.png'))
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
    def __init__(self, Player1, Player2, parent=None):
        super(Game, self).__init__(parent)
        self.setFixedSize(645, 415)
        self.setWindowTitle("King of Siam")
        self.setStyleSheet("background-color: #2d3436; color: white; font-size: 18px;")
        self.setWindowIcon(QtGui.QIcon('./content/boulder.png'))
        self.title = QtWidgets.QLabel(self)

        self.title.setText("King of Siam")
        self.title.setStyleSheet("font-size: 41px; font-family: Bradley Hand ITC; font-weight: bold; color: #ee5253;")
        self.title.setGeometry(375, 10, 300, 50)

        self.namePlayer1 = Player1
        self.namePlayer2 = Player2

        # Game setup
        self.g = GameMap()
        if self.g.playerTurn == 'Elephant':
            self.currentPlayer1 = True
        else:
            self.currentPlayer1 = False
        self.ndir = np.array([1, 0])
        self.ndirDeg = 0

        self.startpoint = True
        self.selectValid = False

        # Showing the gamemap
        label = QtWidgets.QLabel(self)
        Pixmap = QtGui.QPixmap('./content/gamemap.png')
        label.setPixmap(Pixmap)
        label.setGeometry(10, 5, 360, 360)

        self.setTiles()
        self.refresh()

        # Creating the buttons
        self.cancelButton()
        self.deleteButton()
        self.validButton()
        self.playerBoard()
        self.turnWidget()
        self.saveWidget()

        self.show()

    def mousePressEvent(self, event):
        isel, jsel = int((event.y() - 15) / 66.5), int((event.x() - 15) / 66.5)

        if event.button() == Qt.LeftButton and 0 <= isel <= 4 and 0 <= jsel <= 4:
            if self.startpoint and self.g[isel][jsel] != 0 and self.g[isel][jsel].species != 'Boulder' and (self.currentPlayer1 and self.g[isel][jsel].species == 'Elephant' or not self.currentPlayer1 and self.g[isel][jsel].species == 'Rhinoceros'):
                self.starti, self.startj = isel, jsel
                self.endi, self.endj = isel, jsel
                for j in range(5):
                    for i in range(5):
                        self.tile[i][j].setStyleSheet("background-color: rgba(0, 0, 0, 0%);")

                li = [-1, 0, 1]
                l = [(self.starti+x, self.startj+y) for x in li for y in li if 0 <= self.starti+x < 5 and 0 <= self.startj+y < 5 and abs(x*y) != 1]
                for k in l:
                    m, n = k
                    self.tile[m][n].setStyleSheet("background-color: #ff9f43")

                self.playerTile.setPixmap(QtGui.QPixmap('./content/transparent.png'))
                self.tile[self.starti][self.startj].setStyleSheet("background-color: #ff9f43")
                self.startpoint = False
                self.buttonCancel.setEnabled(True)
                self.buttonValid.setDisabled(True)
                self.button90l.setDisabled(True)
                self.button90r.setDisabled(True)
                self.playerTile.setStyleSheet("background-color: #353b48")
            elif not self.startpoint:
                li = [-1, 0, 1]
                l = [(self.starti + x, self.startj + y) for x in li for y in li if 0 <= self.starti+x < 5 and 0 <= self.startj+y < 5 and abs(x * y) != 1]
                self.endi, self.endj = int((event.y()-10)/66.5), int((event.x()-15)/66.5)

                if (self.endi, self.endj) in l:
                    self.selectValid = True
                    self.startpoint = True
                    self.tile[self.endi][self.endj].setStyleSheet("background-color: #ee5253")
                    self.buttonValid.setEnabled(True)
                    self.button90l.setEnabled(True)
                    self.button90r.setEnabled(True)
                    self.playerTile.setStyleSheet("background-color: #ff9f43")
                    self.setPlayerTile(self.starti, self.startj)

                    if self.starti == self.endi and self.startj == self.endj and self.g[self.starti][self.startj] != 0:
                        self.buttonDelete.setEnabled(True)

            elif self.g[isel][jsel] == 0 and (isel == 4 or isel == 0 or jsel == 4 or jsel == 0):
                self.starti, self.startj = isel, jsel
                self.endi, self.endj = isel, jsel
                for j in range(5):
                    for i in range(5):
                        self.tile[i][j].setStyleSheet("background-color: rgba(0, 0, 0, 0%);")
                self.tile[self.starti][self.startj].setStyleSheet("background-color: #ee5253")
                self.buttonValid.setEnabled(True)
                self.button90l.setEnabled(True)
                self.button90r.setEnabled(True)
                self.buttonCancel.setEnabled(True)
                self.playerTile.setStyleSheet("background-color: #ff9f43")
                self.setPlayerTile(self.starti, self.startj)

    def cancelButton(self):
        self.buttonCancel = QtWidgets.QPushButton('Cancel', self)
        self.buttonCancel.setStyleSheet("QPushButton {"
                                            "height: 30px; font-size: 18px; color: white; margin-top: 6px;"
                                            "text-align: center; background: #e74c3c; border: 0;"
                                            "border-bottom: 3px solid #c0392b; border-right: 3px solid #c0392b;}"
                                       "QPushButton:pressed {"
                                            "border: 0px; background: #c0392b;}"
                                       "QPushButton:!enabled {"
                                            "background-color: #353b48; border: 0;"
                                            "border-bottom: 3px solid #2f3640; border-right: 3px solid #2f3640;}")
        self.buttonCancel.setGeometry(380, 235, 250, 40)
        self.buttonCancel.clicked.connect(lambda: self.cancelButtonClicked())
        self.buttonCancel.setDisabled(True)

    def cancelButtonClicked(self):
        for j in range(5):
            for i in range(5):
                self.tile[i][j].setStyleSheet("background-color: rgba(0, 0, 0, 0%);")
        self.startpoint = True
        self.buttonCancel.setDisabled(True)
        self.buttonValid.setDisabled(True)
        self.button90l.setDisabled(True)
        self.button90r.setDisabled(True)
        self.playerTile.setStyleSheet("background-color: #353b48")
        self.playerTile.clear()

    def deleteButton(self):
        self.buttonDelete = QtWidgets.QPushButton('Delete Animal', self)
        self.buttonDelete.setStyleSheet("QPushButton {"
                                            "height: 30px; font-size: 18px; color: white; margin-top: 6px;"
                                            "text-align: center; background: #e74c3c; border: 0;"
                                            "border-bottom: 3px solid #c0392b; border-right: 3px solid #c0392b;}"
                                       "QPushButton:pressed {"
                                            "border: 0px; background: #c0392b;}"
                                       "QPushButton:!enabled {"
                                            "background-color: #353b48; border: 0;"
                                            "border-bottom: 3px solid #2f3640; border-right: 3px solid #2f3640;}")
        self.buttonDelete.setGeometry(380, 275, 250, 40)
        self.buttonDelete.clicked.connect(lambda: self.deleteButtonClicked())
        self.buttonDelete.setDisabled(True)

    def deleteButtonClicked(self):
        self.g.delete(self.g[self.starti][self.startj])
        self.startpoint = True
        self.buttonCancel.setDisabled(True)
        self.buttonDelete.setDisabled(True)
        self.buttonValid.setDisabled(True)
        self.button90l.setDisabled(True)
        self.button90r.setDisabled(True)
        self.playerTile.setStyleSheet("background-color: #353b48")
        self.playerTile.clear()
        self.refresh()

    def validButton(self):
        self.buttonValid = QtWidgets.QPushButton('Accept', self)
        self.buttonValid.setStyleSheet("QPushButton {"
                                            "height: 30px; font-size: 18px; color: white; margin-top: 6px;"
                                            "text-align: center; background: #2ecc71; border: 0;"
                                            "border-bottom: 3px solid #27ae60; border-right: 3px solid #27ae60;}"
                                       "QPushButton:pressed {"
                                            "border: 0px; background: #27ae60;}"
                                       "QPushButton:!enabled {"
                                            "background-color: #353b48; border: 0;"
                                            "border-bottom: 3px solid #2f3640; border-right: 3px solid #2f3640;}")
        self.buttonValid.setGeometry(380, 315, 250, 40)
        self.buttonValid.clicked.connect(lambda: self.validButtonClicked())
        self.buttonValid.setDisabled(True)

    def validButtonClicked(self):
        for j in range(5):
            for i in range(5):
                self.tile[i][j].setStyleSheet("background-color: rgba(0, 0, 0, 0%);")

        if self.starti == self.endi and self.startj == self.endj:
            if self.g[self.starti][self.startj] != 0:
                self.g.move(self.g[self.starti][self.startj], (self.endi, self.endj), self.ndir)
            elif (self.starti == 0 or self.starti == 4 or self.startj == 0 or self.startj == 4):
                if self.currentPlayer1:
                    self.g.add(Animal(self.endi, self.endj, self.ndir, "Elephant"))
                else:
                    self.g.add(Animal(self.endi, self.endj, self.ndir, "Rhinoceros"))
        else:  
            self.g.move(self.g[self.starti][self.startj], (self.endi, self.endj), self.ndir)

        self.startpoint = True
        self.buttonCancel.setDisabled(True)
        self.buttonValid.setDisabled(True)
        self.button90l.setDisabled(True)
        self.button90r.setDisabled(True)
        self.playerTile.setStyleSheet("background-color: #353b48")
        self.playerTile.clear()

        print(self.g)

        self.refresh()

    def turnWidget(self):
        self.playerTile = QtWidgets.QLabel(self)
        self.playerTile.setStyleSheet("background-color: #353b48")
        self.playerTile.setGeometry(380, 155, 64, 64)

        self.button90l = QtWidgets.QPushButton('Turn 90° Left', self)
        self.button90l.setStyleSheet("QPushButton {"
                                     "height: 30px; font-size: 18px; color: white; margin-top: 6px;"
                                     "text-align: center; background: #9b59b6; border: 0;"
                                     "border-bottom: 3px solid #8e44ad; border-right: 3px solid #8e44ad;}"
                                     "QPushButton:pressed {"
                                     "border: 0px; background: #8e44ad;}"
                                     "QPushButton:!enabled {"
                                     "background-color: #353b48; border: 0;"
                                     "border-bottom: 3px solid #2f3640; border-right: 3px solid #2f3640;}")
        self.button90l.setGeometry(465, 145, 165, 40)
        self.button90l.clicked.connect(lambda: self.TLeft90())
        self.button90l.setDisabled(True)

        self.button90r = QtWidgets.QPushButton('Turn 90° Right', self)
        self.button90r.setStyleSheet("QPushButton {"
                                     "height: 30px; font-size: 18px; color: white; margin-top: 6px;"
                                     "text-align: center; background: #3498db; border: 0;"
                                     "border-bottom: 3px solid #2980b9; border-right: 3px solid #2980b9;}"
                                     "QPushButton:pressed {"
                                     "border: 0px; background: #2980b9;}"
                                     "QPushButton:!enabled {"
                                     "background-color: #353b48; border: 0;"
                                     "border-bottom: 3px solid #2f3640; border-right: 3px solid #2f3640;}")
        self.button90r.setGeometry(465, 185, 165, 40)
        self.button90r.clicked.connect(lambda: self.TRight90())
        self.button90r.setDisabled(True)

    def saveWidget(self):
        self.buttonLoad = QtWidgets.QPushButton('Load', self)
        self.buttonLoad.setStyleSheet("QPushButton {"
                                     "height: 30px; font-size: 18px; color: white; margin-top: 6px;"
                                     "text-align: center; background: #1abc9c; border: 0;"
                                     "border-bottom: 3px solid #16a085; border-right: 3px solid #16a085;}"
                                     "QPushButton:pressed {"
                                     "border: 0px; background: #16a085;}"
                                     "QPushButton:!enabled {"
                                     "background-color: #353b48; border: 0;"
                                     "border-bottom: 3px solid #2f3640; border-right: 3px solid #2f3640;}")
        self.buttonLoad.setGeometry(15, 365, 300, 40)
        self.buttonLoad.clicked.connect(lambda: self.loadFile())

        self.buttonSave = QtWidgets.QPushButton('Save', self)
        self.buttonSave.setStyleSheet("QPushButton {"
                                      "height: 30px; font-size: 18px; color: white; margin-top: 6px;"
                                      "text-align: center; background: #1abc9c; border: 0;"
                                      "border-bottom: 3px solid #16a085; border-right: 3px solid #16a085;}"
                                      "QPushButton:pressed {"
                                      "border: 0px; background: #16a085;}"
                                      "QPushButton:!enabled {"
                                      "background-color: #353b48; border: 0;"
                                      "border-bottom: 3px solid #2f3640; border-right: 3px solid #2f3640;}")
        self.buttonSave.setGeometry(330, 365, 300, 40)
        self.buttonSave.clicked.connect(lambda: self.saveFile())

    def loadFile(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open King of Siam save', '/home')
        if fname[0]:
            f = open(fname[0], 'r')
            self.g.load(f)
            self.refresh()

    def saveFile(self):
        fname = QtWidgets.QFileDialog.getSaveFileName(self, 'Save King of Siam save', '/home')
        if fname[0]:
            file = open(fname[0], 'w')
            self.g.save(file)

    def TLeft90(self):
        dirs = [np.array([1, 0]), np.array([0, -1]), np.array([-1, 0]), np.array([0, 1])]
        dirdeg = [270, 180, 90, 0]
        self.ndirDeg = dirdeg[dirdeg.index(self.ndirDeg) % len(dirdeg)-1]
        self.ndir = dirs[dirdeg.index(self.ndirDeg)]

        if self.currentPlayer1 :
            path = "./content/elephant/elephant_" + str(self.ndirDeg) + ".png"
        else:
            path = "./content/rhinoceros/rhinoceros_" + str(self.ndirDeg) + ".png"
        self.playerTile.setPixmap(QtGui.QPixmap(path))

    def TRight90(self):
        dirs = [np.array([1, 0]), np.array([0, 1]), np.array([-1, 0]), np.array([0, -1])]
        dirdeg = [270, 0, 90, 180]
        self.ndirDeg = dirdeg[dirdeg.index(self.ndirDeg) % len(dirdeg)-1]
        self.ndir = dirs[dirdeg.index(self.ndirDeg)]

        if self.currentPlayer1:
            path = "./content/elephant/elephant_" + str(self.ndirDeg) + ".png"
        else:
            path = "./content/rhinoceros/rhinoceros_" + str(self.ndirDeg) + ".png"
        self.playerTile.setPixmap(QtGui.QPixmap(path))

    def playerBoard(self):
        self.Elephanttitle = QtWidgets.QLabel(self)
        self.Elephanttitle.setText("Elephant :")
        self.Elephanttitle.setStyleSheet("font-size: 18px; font-family: Tahoma; font-weight: bold;")
        self.Elephanttitle.setGeometry(375, 80, 300, 20)

        self.Elephantname = QtWidgets.QLabel(self)
        self.Elephantname.setText(self.namePlayer1)
        self.Elephantname.setStyleSheet("font-size: 18px; font-family: Tahoma; color: #0984e3; font-weight: bold;")
        self.Elephantname.setGeometry(500, 80, 300, 20)

        self.Rhinocerostitle = QtWidgets.QLabel(self)
        self.Rhinocerostitle.setText("Rhinoceros :")
        self.Rhinocerostitle.setStyleSheet("font-size: 18px; font-family: Tahoma; font-weight: bold;")
        self.Rhinocerostitle.setGeometry(375, 110, 300, 16)

        self.Rhinocerosname = QtWidgets.QLabel(self)
        self.Rhinocerosname.setText(self.namePlayer2)
        self.Rhinocerosname.setStyleSheet("font-size: 18px; font-family: Tahoma; color: #d63031; font-weight: bold;")
        self.Rhinocerosname.setGeometry(500, 110, 300, 20)

    def setPlayerTile(self, i, j):

        if self.g[i][j] == 0:
            if self.currentPlayer1 :
                Pixmap = QtGui.QPixmap("./content/elephant/elephant_270.png")
            else:
                Pixmap = QtGui.QPixmap("./content/rhinoceros/rhinoceros_270.png")
            self.playerTile.setPixmap(Pixmap)
            self.ndir = np.array([1, 0])
            self.ndirDeg = 270
        else:
            s = self.g[i][j].species
            dir = self.g[i][j].direction
            if s == 'Elephant':
                if dir[0] == 1 and dir[1] == 0:
                    Pixmap = QtGui.QPixmap("./content/elephant/elephant_270.png")
                    self.playerTile.setPixmap(Pixmap)
                    self.ndir = np.array([1, 0])
                    self.ndirDeg = 270
                elif dir[0] == -1 and dir[1] == 0:
                    Pixmap = QtGui.QPixmap("./content/elephant/elephant_90.png")
                    self.playerTile.setPixmap(Pixmap)
                    self.ndir = np.array([-1, 0])
                    self.ndirDeg = 90
                elif dir[0] == 0 and dir[1] == -1:
                    Pixmap = QtGui.QPixmap("./content/elephant/elephant_180.png")
                    self.playerTile.setPixmap(Pixmap)
                    self.ndir = np.array([0, -1])
                    self.ndirDeg = 180
                elif dir[0] == 0 and dir[1] == 1:
                    Pixmap = QtGui.QPixmap("./content/elephant/elephant_0.png")
                    self.playerTile.setPixmap(Pixmap)
                    self.ndir = np.array([0, 1])
                    self.ndirDeg = 0
            elif s == 'Rhinoceros':
                if dir[0] == 1 and dir[1] == 0:
                    Pixmap = QtGui.QPixmap("./content/rhinoceros/rhinoceros_270.png")
                    self.playerTile.setPixmap(Pixmap)
                    self.ndir = np.array([1, 0])
                    self.ndirDeg = 270
                elif dir[0] == 0 and dir[1] == 1:
                    Pixmap = QtGui.QPixmap("./content/rhinoceros/rhinoceros_0.png")
                    self.playerTile.setPixmap(Pixmap)
                    self.ndir = np.array([0, 1])
                    self.ndirDeg = 0
                elif dir[0] == -1 and dir[1] == 0:
                    Pixmap = QtGui.QPixmap("./content/rhinoceros/rhinoceros_90.png")
                    self.playerTile.setPixmap(Pixmap)
                    self.ndir = np.array([-1, 0])
                    self.ndirDeg = 90
                elif dir[0] == 0 and dir[1] == -1:
                    Pixmap = QtGui.QPixmap("./content/rhinoceros/rhinoceros_180.png")
                    self.playerTile.setPixmap(Pixmap)
                    self.ndir = np.array([0, -1])
                    self.ndirDeg = 180

    def setTiles(self):
        xcoords, ycoords = [15, 84, 153, 222, 291], [15, 84, 153, 222, 291]
        self.coord = [[(y, x) for x in xcoords] for y in ycoords]

        self.tile = []
        for i in range(5):
            l = []
            for j in range (5):
                label = QtWidgets.QLabel(self)
                label.setStyleSheet("background-color: rgba(0, 0, 0, 0%);")
                x, y = self.coord[j][i]
                label.setGeometry(x, y, 64, 64)
                label.show()
                l.append(label)
            self.tile.append(l)

    def refresh(self):
        for i in range(5):
            for j in range(5):
                if self.g[i][j] == 0:
                    self.tile[i][j].setPixmap(QtGui.QPixmap('./content/transparent.png'))
                elif self.g[i][j].species == 'Boulder':
                    self.tile[i][j].setPixmap(QtGui.QPixmap('./content/boulder.png'))
                elif self.g[i][j].species == 'Rhinoceros':
                    if self.g[i][j].direction[0] == 1 and self.g[i][j].direction[1] == 0:
                        Pixmap = QtGui.QPixmap("./content/rhinoceros/rhinoceros_270.png")
                        self.tile[i][j].setPixmap(Pixmap)
                    elif self.g[i][j].direction[0] == 0 and self.g[i][j].direction[1] == 1:
                        Pixmap = QtGui.QPixmap("./content/rhinoceros/rhinoceros_0.png")
                        self.tile[i][j].setPixmap(Pixmap)
                    elif self.g[i][j].direction[0] == -1 and self.g[i][j].direction[1] == 0:
                        Pixmap = QtGui.QPixmap("./content/rhinoceros/rhinoceros_90.png")
                        self.tile[i][j].setPixmap(Pixmap)
                    elif self.g[i][j].direction[0] == 0 and self.g[i][j].direction[1] == -1:
                        Pixmap = QtGui.QPixmap("./content/rhinoceros/rhinoceros_180.png")
                        self.tile[i][j].setPixmap(Pixmap)
                elif self.g[i][j].species == 'Elephant':
                    if self.g[i][j].direction[0] == 1 and self.g[i][j].direction[1] == 0:
                        Pixmap = QtGui.QPixmap("./content/elephant/elephant_270.png")
                        self.tile[i][j].setPixmap(Pixmap)
                    elif self.g[i][j].direction[0] == 0 and self.g[i][j].direction[1] == 1:
                        Pixmap = QtGui.QPixmap("./content/elephant/elephant_0.png")
                        self.tile[i][j].setPixmap(Pixmap)
                    elif self.g[i][j].direction[0] == -1 and self.g[i][j].direction[1] == 0:
                        Pixmap = QtGui.QPixmap("./content/elephant/elephant_90.png")
                        self.tile[i][j].setPixmap(Pixmap)
                    elif self.g[i][j].direction[0] == 0 and self.g[i][j].direction[1] == -1:
                        Pixmap = QtGui.QPixmap("./content/elephant/elephant_180.png")
                        self.tile[i][j].setPixmap(Pixmap)
                self.tile[i][j].setStyleSheet("background-color: rgba(0, 0, 0, 0%);")
                self.tile[i][j].show()

        if self.g.playerTurn == 'Elephant':
            self.currentPlayer1 = True
        else:
            self.currentPlayer1 = False

        if self.g.winner != "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            if self.g.winner == "Elephant":
                msg.setText("The winner is " + self.namePlayer1)
            else:
                msg.setText("The winner is " + self.namePlayer2)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    #login = Login()

    #if login.exec_() == QtWidgets.QDialog.Accepted:
        #eName, rName = login.eName.text(), login.rName.text()
    eName, rName = "Teusner", "Faroluca"
    gwin = Game(eName, rName)
    gwin.show()
    sys.exit(app.exec_())
