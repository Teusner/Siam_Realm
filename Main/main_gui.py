from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt

import random as rd


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
        self.setFixedSize(650, 415)
        self.setWindowTitle("King of Siam")
        self.setStyleSheet("background-color: #2d3436; color: white; font-size: 18px;")
        self.setWindowIcon(QtGui.QIcon('./content/rock.png'))
        self.title = QtWidgets.QLabel(self)
        self.title.setText("King of Siam")
        self.title.setStyleSheet("font-size: 41px; font-family: Bradley Hand ITC; font-weight: bold;")
        self.title.setGeometry(375, 10, 300, 50)

        self.Playertitle = QtWidgets.QLabel(self)
        self.Playertitle.setText("Players")
        self.Playertitle.setStyleSheet("font-size: 20px; font-family: Tahoma; font-weight: bold;")
        self.Playertitle.setGeometry(375, 60, 100, 25)

        self.Elephanttitle = QtWidgets.QLabel(self)
        self.Elephanttitle.setText("Elephant :")
        self.Elephanttitle.setStyleSheet("font-size: 16px; font-family: Tahoma; font-weight: bold;")
        self.Elephanttitle.setGeometry(375, 90, 300, 20)

        self.Elephantname = QtWidgets.QLabel(self)
        self.Elephantname.setText("Teusner")
        self.Elephantname.setStyleSheet("font-size: 16px; font-family: Tahoma; color: #0984e3; font-weight: bold;")
        self.Elephantname.setGeometry(490, 90, 300, 20)

        self.Rhinocerostitle = QtWidgets.QLabel(self)
        self.Rhinocerostitle.setText("Rhinoceros :")
        self.Rhinocerostitle.setStyleSheet("font-size: 16px; font-family: Tahoma; font-weight: bold;")
        self.Rhinocerostitle.setGeometry(375, 115, 300, 16)

        self.Rhinocerosname = QtWidgets.QLabel(self)
        self.Rhinocerosname.setText("Faroluca")
        self.Rhinocerosname.setStyleSheet("font-size: 16px; font-family: Tahoma; color: #d63031; font-weight: bold;")
        self.Rhinocerosname.setGeometry(490, 115, 300, 20)

        self.playerTile = QtWidgets.QLabel(self)
        Pixmap = QtGui.QPixmap('./content/elephant.png')
        self.playerTile.setPixmap(Pixmap)
        self.playerTile.setStyleSheet("background-color: #8e44ad")
        self.playerTile.setGeometry(380, 155, 64, 64)

        self.button90l = QtWidgets.QPushButton('Turn 90° Left', self)
        self.button90l.setStyleSheet("QPushButton {"
                                        "height: 30px; font-size: 18px; color: white; margin-top: 6px;"
                                        "text-align: center; background: #e74c3c; border: 0;"
                                        "border-bottom: 3px solid #c0392b; border-right: 3px solid #c0392b;}"
                                        "QPushButton:pressed {"
                                        "border: 0px; background: #c0392b;}"
                                        "QPushButton:!enabled {"
                                        "background-color: #353b48; border: 0;"
                                        "border-bottom: 3px solid #2f3640; border-right: 3px solid #2f3640;}")
        self.button90l.setGeometry(465, 145, 160, 40)
        #self.button90l.clicked.connect(lambda: self.cancelButtonClicked())
        #self.button90l.setDisabled(True)

        self.button90r = QtWidgets.QPushButton('Turn 90° Right', self)
        self.button90r.setStyleSheet("QPushButton {"
                                     "height: 30px; font-size: 18px; color: white; margin-top: 6px;"
                                     "text-align: center; background: #e74c3c; border: 0;"
                                     "border-bottom: 3px solid #c0392b; border-right: 3px solid #c0392b;}"
                                     "QPushButton:pressed {"
                                     "border: 0px; background: #c0392b;}"
                                     "QPushButton:!enabled {"
                                     "background-color: #353b48; border: 0;"
                                     "border-bottom: 3px solid #2f3640; border-right: 3px solid #2f3640;}")
        self.button90r.setGeometry(465, 185, 160, 40)
        # self.button90r.clicked.connect(lambda: self.cancelButtonClicked())
        #self.button90r.setDisabled(True)

        self.startpoint = True
        self.selectValid = False

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
                elephPixmap = QtGui.QPixmap('./content/elephant.png')
                rhinoPixmap = QtGui.QPixmap('./content/rhinoceros.png')
                boulderPixmap = QtGui.QPixmap('./content/boulder.png')
                r = rd.random()
                if r<0.1:
                    label.setPixmap(elephPixmap)
                elif r<0.2 and r>0.1:
                    label.setPixmap(rhinoPixmap)
                elif r<0.3 and r>0.2:
                    label.setPixmap(boulderPixmap)
                label.setStyleSheet("background-color: rgba(0, 0, 0, 0%);")
                x, y = self.coord[i][j]
                label.setGeometry(x, y, 64, 64)
                l.append(label)
            self.tile.append(l)


        layout = QtWidgets.QVBoxLayout(self)

        # Creating the buttons
        self.cancelButton()
        self.validButton()

        layoutButtons = QtWidgets.QHBoxLayout()
        layoutButtons.addWidget(self.buttonCancel)
        layoutButtons.addWidget(self.buttonValid)

        #layout.addLayout(layoutButtons)

        self.setLayout(layout)


        self.show()

    def mousePressEvent(self, event):
        isel,jsel = int((event.x() - 15) / 66.5), int((event.y() - 15) / 66.5)
        if event.button() == Qt.LeftButton and isel<5 and isel>=0 and jsel<5 and jsel>=0:
            if self.startpoint:
                self.starti, self.startj = isel, jsel
                for j in range(5):
                    for i in range(5):
                        self.tile[i][j].setStyleSheet("background-color: rgba(0, 0, 0, 0%);")

                li = [-1, 0, 1]
                l = [(self.starti+x, self.startj+y) for x in li for y in li if self.starti+x>=0 and self.starti+x<5 and self.startj+y>=0 and self.startj+y<5 and abs(x*y) != 1]
                for k in l:
                    m,n = k
                    self.tile[m][n].setStyleSheet("background-color: #0097e6")

                self.tile[self.starti][self.startj].setStyleSheet("background-color: #8e44ad")
                self.startpoint = False
                self.buttonCancel.setEnabled(True)
                self.buttonValid.setDisabled(True)
            else:
                li = [-1, 0, 1]
                l = [(self.starti + x, self.startj + y) for x in li for y in li if self.starti + x >= 0 and self.starti + x < 5 and self.startj + y >= 0 and self.startj + y < 5 and abs(x * y) != 1]
                self.endi, self.endj = int((event.x()-10)/66.5), int((event.y()-15)/66.5)

                if (self.endi, self.endj) in l:
                    self.selectValid = True
                    self.startpoint = True
                    self.tile[self.endi][self.endj].setStyleSheet("background-color: #f1c40f")
                    self.buttonValid.setEnabled(True)

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
        self.buttonCancel.setGeometry(15, 365, 165, 40)
        self.buttonCancel.clicked.connect(lambda: self.cancelButtonClicked())
        self.buttonCancel.setDisabled(True)

    def cancelButtonClicked(self):
        for j in range(5):
            for i in range(5):
                self.tile[i][j].setStyleSheet("background-color: rgba(0, 0, 0, 0%);")
        self.startpoint = True
        self.buttonCancel.setDisabled(True)
        self.buttonValid.setDisabled(True)

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
        self.buttonValid.setGeometry(190, 365, 165, 40)
        self.buttonValid.clicked.connect(lambda: self.validButtonClicked())
        self.buttonValid.setDisabled(True)

    def validButtonClicked(self):
        for j in range(5):
            for i in range(5):
                self.tile[i][j].setStyleSheet("background-color: rgba(0, 0, 0, 0%);")
        self.startpoint = True
        self.buttonCancel.setDisabled(True)
        self.buttonValid.setDisabled(True)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    """login = Login()

    eName, rName = login.eName.text(), login.rName.text()

    if login.exec_() == QtWidgets.QDialog.Accepted:"""
    gwin = Game()
    gwin.show()
    sys.exit(app.exec_())
