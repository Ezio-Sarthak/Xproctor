# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StudentMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StudentMainWindow(object):
    def setupUi(self, StudentMainWindow):
        StudentMainWindow.setObjectName("StudentMainWindow")
        StudentMainWindow.resize(726, 583)
        self.centralwidget = QtWidgets.QWidget(StudentMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(378, 24, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.timeRemaining = QtWidgets.QLineEdit(self.frame)
        self.timeRemaining.setObjectName("timeRemaining")
        self.horizontalLayout.addWidget(self.timeRemaining)
        spacerItem1 = QtWidgets.QSpacerItem(58, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 437, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(378, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.finishExamButton = QtWidgets.QPushButton(self.centralwidget)
        self.finishExamButton.setObjectName("finishExamButton")
        self.horizontalLayout_3.addWidget(self.finishExamButton)
        spacerItem4 = QtWidgets.QSpacerItem(378, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        StudentMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(StudentMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 726, 20))
        self.menubar.setObjectName("menubar")
        self.menuFIle = QtWidgets.QMenu(self.menubar)
        self.menuFIle.setObjectName("menuFIle")
        StudentMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(StudentMainWindow)
        self.statusbar.setObjectName("statusbar")
        StudentMainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(StudentMainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFIle.addAction(self.actionExit)
        self.menubar.addAction(self.menuFIle.menuAction())

        self.retranslateUi(StudentMainWindow)
        QtCore.QMetaObject.connectSlotsByName(StudentMainWindow)

    def retranslateUi(self, StudentMainWindow):
        _translate = QtCore.QCoreApplication.translate
        StudentMainWindow.setWindowTitle(_translate("StudentMainWindow", "StudentMainWindow"))
        self.label.setText(_translate("StudentMainWindow", "Time remaining:"))
        self.timeRemaining.setText(_translate("StudentMainWindow", "00"))
        self.finishExamButton.setText(_translate("StudentMainWindow", "Finish Exam"))
        self.menuFIle.setTitle(_translate("StudentMainWindow", "FIle"))
        self.actionExit.setText(_translate("StudentMainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StudentMainWindow = QtWidgets.QMainWindow()
    ui = Ui_StudentMainWindow()
    ui.setupUi(StudentMainWindow)
    StudentMainWindow.show()
    sys.exit(app.exec_())

