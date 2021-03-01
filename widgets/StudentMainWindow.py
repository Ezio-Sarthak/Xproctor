# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StudentMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os, sys, cv2
from datetime import datetime
from threading import Timer
import pyscreenshot, qpageview


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
        self.finishExamButton.clicked.connect(self.finishExam)
        self.horizontalLayout_3.addWidget(self.finishExamButton)
        spacerItem4 = QtWidgets.QSpacerItem(378, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        StudentMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(StudentMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 726, 20))
        self.menubar.setObjectName("menubar")
        StudentMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(StudentMainWindow)
        self.statusbar.setObjectName("statusbar")
        StudentMainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(StudentMainWindow)
        QtCore.QMetaObject.connectSlotsByName(StudentMainWindow)

        checkOverlay()

        # Below code will start wevcam for proctoring

        # # This will return video from the first webcam on your computer.
        # try:
        #     cap = cv2.VideoCapture(0)
        # except:
        #     print("Error message", "Your system doesn't have active Webcam avaiable. Exiting.")
        #     sys.exit(0)

        # # Define the codec and create VideoWriter object
        # fourcc = cv2.VideoWriter_fourcc(*'XVID')
        # out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
        # captureVideo(cap, out, fourcc)
        # cap.release()

        # # After we release our webcam, we also release the output
        # out.release()

        # # De-allocate any associated memory usage
        # cv2.destroyAllWindows()

    def finishExam(self):
        # Code here to send report after encryption
        print('Paper Finished! report will be sent after encryption')

    def retranslateUi(self, StudentMainWindow):
        _translate = QtCore.QCoreApplication.translate
        StudentMainWindow.setWindowTitle(_translate("StudentMainWindow", "StudentMainWindow"))
        self.label.setText(_translate("StudentMainWindow", "Time remaining: 00"))
        self.finishExamButton.setText(_translate("StudentMainWindow", "Finish Exam"))

# Current Window ID
THIS_WINDOW_NAME = 'StudentMainWindow'

def stdout(cmd: str):
    output = str(os.popen(cmd).read())
    # Truncate the output string (original: '<output>\n')
    return output[:-1]

def captureScreenShot():
    DIR = "screenshots"

    # If the directory doesn't exists, create it
    if not os.path.isdir(DIR):
        os.mkdir(DIR)

    # Set filename as the timestamp of capture
    date = datetime.now().replace(microsecond=0)
    path = f"{DIR}/Screenshot from {date}.png"

    # Capture and save the screenshot
    pyscreenshot.grab().save(path)

def checkOverlay():
    win_name = stdout("xprop -id $(xprop -root 32x '\t$0' _NET_ACTIVE_WINDOW | cut -f 2) _NET_WM_NAME | cut -d '\"' -f 2")

    if win_name != THIS_WINDOW_NAME:
        captureScreenShot()

    Timer(2, checkOverlay).start()


def captureVideo(cap, out, fourcc):

    # reads frames from a camera
    # ret checks return at each frame
    ret, frame = cap.read()

    # output the frame
    out.write(frame)

    checkOverlay(cap, out)

    Timer(1, captureVideo(cap, out, fourcc)).start()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    StudentMainWindow = QtWidgets.QMainWindow()
    ui = Ui_StudentMainWindow()
    ui.setupUi(StudentMainWindow)
    StudentMainWindow.showMaximized()
    StudentMainWindow.setFixedSize(StudentMainWindow.width(), StudentMainWindow.height())
    StudentMainWindow.show()
    sys.exit(app.exec_())
