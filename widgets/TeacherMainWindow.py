# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TeacherMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from FileOpenDialog import App

class Ui_TeacherMainWindow(object):
    def setupUi(self, TeacherMainWindow):
        TeacherMainWindow.setObjectName("TeacherMainWindow")
        TeacherMainWindow.resize(350, 459)
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
        self.filePath = QtWidgets.QLabel(self.frame)
        self.filePath.setAlignment(QtCore.Qt.AlignCenter)
        self.filePath.setObjectName("filePath")
        self.gridLayout.addWidget(self.filePath, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.submitQPaper = QtWidgets.QPushButton(self.centralwidget)
        self.submitQPaper.setObjectName("submitQPaper")
        self.horizontalLayout.addWidget(self.submitQPaper)
        spacerItem1 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.uploadQPaperButton = QtWidgets.QToolButton(self.centralwidget)
        self.uploadQPaperButton.setObjectName("uploadQPaperButton")
        self.uploadQPaperButton.clicked.connect(self.uploadFileWindow)
        self.horizontalLayout.addWidget(self.uploadQPaperButton)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(92, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 2, 1, 1)
        TeacherMainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(TeacherMainWindow)
        self.statusbar.setObjectName("statusbar")
        TeacherMainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(TeacherMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 350, 20))
        self.menubar.setObjectName("menubar")
        TeacherMainWindow.setMenuBar(self.menubar)
        self.actionStart = QtWidgets.QAction(TeacherMainWindow)
        self.actionStart.setObjectName("actionStart")
        self.actionExit = QtWidgets.QAction(TeacherMainWindow)
        self.actionExit.setObjectName("actionExit")

        self.retranslateUi(TeacherMainWindow)
        QtCore.QMetaObject.connectSlotsByName(TeacherMainWindow)

    def uploadFileWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = App()
        self.filePath.setText(self.ui.file_name)

    def retranslateUi(self, TeacherMainWindow):
        _translate = QtCore.QCoreApplication.translate
        TeacherMainWindow.setWindowTitle(_translate("TeacherMainWindow", "TeacherMainWindow"))
        self.label.setText(_translate("TeacherMainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Welcome to the Teacher\'s section!</span></p></body></html>"))
        self.filePath.setText(_translate("TeacherMainWindow", "(Not selected)"))
        self.submitQPaper.setText(_translate("TeacherMainWindow", "Upload question paper"))
        self.uploadQPaperButton.setText(_translate("TeacherMainWindow", "..."))
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

