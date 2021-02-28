# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TeacherMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TeacherMainWindow(object):
    def setupUi(self, TeacherMainWindow):
        TeacherMainWindow.setObjectName("TeacherMainWindow")
        TeacherMainWindow.resize(365, 244)
        self.centralwidget = QtWidgets.QWidget(TeacherMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        self.uploadQuePaperButton = QtWidgets.QPushButton(self.centralwidget)
        self.uploadQuePaperButton.setObjectName("uploadQuePaperButton")
        self.gridLayout_2.addWidget(self.uploadQuePaperButton, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(92, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 2, 1, 1)
        TeacherMainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(TeacherMainWindow)
        self.statusbar.setObjectName("statusbar")
        TeacherMainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(TeacherMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 365, 20))
        self.menubar.setObjectName("menubar")
        TeacherMainWindow.setMenuBar(self.menubar)
        self.actionStart = QtWidgets.QAction(TeacherMainWindow)
        self.actionStart.setObjectName("actionStart")
        self.actionExit = QtWidgets.QAction(TeacherMainWindow)
        self.actionExit.setObjectName("actionExit")

        self.retranslateUi(TeacherMainWindow)
        QtCore.QMetaObject.connectSlotsByName(TeacherMainWindow)

    def retranslateUi(self, TeacherMainWindow):
        _translate = QtCore.QCoreApplication.translate
        TeacherMainWindow.setWindowTitle(_translate("TeacherMainWindow", "TeacherMainWindow"))
        self.label.setText(_translate("TeacherMainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Welcome to the Teacher\'s section!</span></p></body></html>"))
        self.uploadQuePaperButton.setText(_translate("TeacherMainWindow", "Upload question paper"))
        self.actionStart.setText(_translate("TeacherMainWindow", "Start"))
        self.actionExit.setText(_translate("TeacherMainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TeacherMainWindow = QtWidgets.QMainWindow()
    ui = Ui_TeacherMainWindow()
    ui.setupUi(TeacherMainWindow)
    TeacherMainWindow.show()
    sys.exit(app.exec_())

