# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'past_sessions.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(833, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(833, 500))
        MainWindow.setMaximumSize(QtCore.QSize(833, 500))
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 120, 225, 255), stop:0.5 rgba(0, 120, 225, 255), stop:1 rgba(40, 145, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sessionList = QtWidgets.QListWidget(self.centralwidget)
        self.sessionList.setEnabled(False)
        self.sessionList.setGeometry(QtCore.QRect(10, 10, 451, 491))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.sessionList.setFont(font)
        self.sessionList.setStyleSheet("QListWidget {background-color: rgba(0, 0, 0, 0); color: rgba(255, 255, 255, 100);}\n"
"\n"
"QListWidget::item\n"
"{\n"
"    background: rgba(0, 0, 0, 0);\n"
"}\n"
"\n"
"QListWidget::item:selected\n"
"{\n"
"    background: rgba(0, 0, 0, 0);\n"
"}")
        self.sessionList.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.sessionList.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.sessionList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.sessionList.setObjectName("sessionList")
        self.detailsButton = QtWidgets.QPushButton(self.centralwidget)
        self.detailsButton.setGeometry(QtCore.QRect(560, 10, 171, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.detailsButton.setFont(font)
        self.detailsButton.setStyleSheet("QPushButton {background-color: rgba(0, 0, 0, 0); color: rgba(159, 208, 255, 255); border-radius: 20px; border-style: solid; border-color: rgba(159, 208, 255, 255); border-width: 2px;}\n"
"QPushButton::hover::!pressed {background-color: rgba(20, 25, 80, 0); color: rgba(255, 255, 255, 255); border-color: rgba(255, 255, 255, 255)}\n"
"QPushButton::pressed {background-color: rgba(255, 255, 255, 255)};")
        self.detailsButton.setCheckable(False)
        self.detailsButton.setChecked(False)
        self.detailsButton.setFlat(False)
        self.detailsButton.setObjectName("detailsButton")
        self.finalMistakes = QtWidgets.QLabel(self.centralwidget)
        self.finalMistakes.setGeometry(QtCore.QRect(490, 110, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(30)
        self.finalMistakes.setFont(font)
        self.finalMistakes.setStyleSheet("background-color: rgba(32, 32, 32, 0); color: rgba(255, 255, 255, 100);\n"
"border-radius: 20px;\n"
"border-style: solid;\n"
"border-color: rgba(159, 208, 255, 255);\n"
"border-width: 4px;")
        self.finalMistakes.setAlignment(QtCore.Qt.AlignCenter)
        self.finalMistakes.setObjectName("finalMistakes")
        self.finalSpeed = QtWidgets.QLabel(self.centralwidget)
        self.finalSpeed.setGeometry(QtCore.QRect(490, 220, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(30)
        self.finalSpeed.setFont(font)
        self.finalSpeed.setStyleSheet("background-color: rgba(32, 32, 32, 0); color: rgba(255, 255, 255, 100);\n"
"border-radius: 20px;\n"
"border-style: solid;\n"
"border-color: rgba(159, 208, 255, 255);\n"
"border-width: 4px;")
        self.finalSpeed.setAlignment(QtCore.Qt.AlignCenter)
        self.finalSpeed.setObjectName("finalSpeed")
        self.finalTime = QtWidgets.QLabel(self.centralwidget)
        self.finalTime.setGeometry(QtCore.QRect(490, 320, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(30)
        self.finalTime.setFont(font)
        self.finalTime.setStyleSheet("background-color: rgba(32, 32, 32, 0); color: rgba(255, 255, 255, 100);\n"
"border-radius: 20px;\n"
"border-style: solid;\n"
"border-color: rgba(159, 208, 255, 255);\n"
"border-width: 4px;")
        self.finalTime.setAlignment(QtCore.Qt.AlignCenter)
        self.finalTime.setObjectName("finalTime")
        self.graphWidget = PlotWidget(self.centralwidget)
        self.graphWidget.setGeometry(QtCore.QRect(470, 80, 361, 421))
        self.graphWidget.setStyleSheet("")
        self.graphWidget.setObjectName("graphWidget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.detailsButton.setText(_translate("MainWindow", "Details"))
        self.finalMistakes.setText(_translate("MainWindow", "TextLabel"))
        self.finalSpeed.setText(_translate("MainWindow", "TextLabel"))
        self.finalTime.setText(_translate("MainWindow", "TextLabel"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
