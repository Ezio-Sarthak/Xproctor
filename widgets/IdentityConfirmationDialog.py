# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IdentityConfirmationDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_IdentityConfirmationDialog(object):
    def setupUi(self, IdentityConfirmationDialog):
        IdentityConfirmationDialog.setObjectName("IdentityConfirmationDialog")
        IdentityConfirmationDialog.resize(369, 157)
        self.gridLayout = QtWidgets.QGridLayout(IdentityConfirmationDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(IdentityConfirmationDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.studentButton = QtWidgets.QPushButton(IdentityConfirmationDialog)
        self.studentButton.setObjectName("studentButton")
        self.gridLayout.addWidget(self.studentButton, 1, 0, 1, 1)
        self.teacherButton = QtWidgets.QPushButton(IdentityConfirmationDialog)
        self.teacherButton.setObjectName("teacherButton")
        self.gridLayout.addWidget(self.teacherButton, 1, 2, 1, 1)

        self.retranslateUi(IdentityConfirmationDialog)
        QtCore.QMetaObject.connectSlotsByName(IdentityConfirmationDialog)

    def retranslateUi(self, IdentityConfirmationDialog):
        _translate = QtCore.QCoreApplication.translate
        IdentityConfirmationDialog.setWindowTitle(_translate("IdentityConfirmationDialog", "Dialog"))
        self.label.setText(_translate("IdentityConfirmationDialog", "What is your identity?"))
        self.studentButton.setText(_translate("IdentityConfirmationDialog", "Student"))
        self.teacherButton.setText(_translate("IdentityConfirmationDialog", "Teacher"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    IdentityConfirmationDialog = QtWidgets.QDialog()
    ui = Ui_IdentityConfirmationDialog()
    ui.setupUi(IdentityConfirmationDialog)
    IdentityConfirmationDialog.show()
    sys.exit(app.exec_())

