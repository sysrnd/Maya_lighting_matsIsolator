# -*- coding: utf-8 -*-



# Form implementation generated from reading ui file 'mats_Isolator_v01.ui'

#

# Created by: PyQt4 UI code generator 4.11.4

#

# WARNING! All changes made in this file will be lost!



from Modules.Qt import QtCore, QtGui, QtWidgets


try:

    _encoding = QtWidgets.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):

        return QtCore.QCoreApplication.translate(context, text, disambig, _encoding)

except AttributeError:

    def _translate(context, text, disambig):

        return QtCore.QCoreApplication.translate(context, text, disambig)



class Ui_window_mats_Isolator(object):

    def setupUi(self, window_mats_Isolator):

        window_mats_Isolator.setObjectName("window_mats_Isolator")

        window_mats_Isolator.resize(545, 671)

        self.centralwidget = QtWidgets.QWidget(window_mats_Isolator)

        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)

        self.gridLayout_2.setObjectName("gridLayout_2")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()

        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.label = QtWidgets.QLabel(self.centralwidget)

        font = QtGui.QFont()

        font.setPointSize(12)

        font.setBold(False)

        font.setWeight(50)

        self.label.setFont(font)

        self.label.setObjectName("label")

        self.horizontalLayout_2.addWidget(self.label)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)

        font = QtGui.QFont()

        font.setPointSize(12)

        font.setBold(False)

        font.setWeight(50)

        self.label_2.setFont(font)

        self.label_2.setObjectName("label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.horizontalLayout = QtWidgets.QHBoxLayout()

        self.horizontalLayout.setObjectName("horizontalLayout")

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)

        self.listWidget.setObjectName("listWidget")

        self.horizontalLayout.addWidget(self.listWidget)

        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)

        self.listWidget_2.setObjectName("listWidget_2")

        self.horizontalLayout.addWidget(self.listWidget_2)

        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)

        self.pushButton.setMinimumSize(QtCore.QSize(0, 60))

        self.pushButton.setObjectName("pushButton")

        self.gridLayout_2.addWidget(self.pushButton, 2, 0, 1, 1)

        window_mats_Isolator.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(window_mats_Isolator)

        self.menubar.setGeometry(QtCore.QRect(0, 0, 545, 21))

        self.menubar.setObjectName("menubar")

        window_mats_Isolator.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(window_mats_Isolator)

        self.statusbar.setObjectName("statusbar")

        window_mats_Isolator.setStatusBar(self.statusbar)



        self.retranslateUi(window_mats_Isolator)

        QtCore.QMetaObject.connectSlotsByName(window_mats_Isolator)



    def retranslateUi(self, window_mats_Isolator):

        window_mats_Isolator.setWindowTitle(_translate("window_mats_Isolator", "Materials Isolator", None))

        self.label.setText(_translate("window_mats_Isolator", "Geometry", None))

        self.label_2.setText(_translate("window_mats_Isolator", "Unassigned materials", None))

        self.pushButton.setText(_translate("window_mats_Isolator", "Assign", None))



