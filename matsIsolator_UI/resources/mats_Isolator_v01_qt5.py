# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Z:\RnD\Pipeline\Maya\Scripts\Lighting\Maya_lighting_matsIsolator\matsIsolator_UI\resources\mats_Isolator_v01.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

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
        self.lyt_grid_main = QtWidgets.QWidget(window_mats_Isolator)
        self.lyt_grid_main.setObjectName("lyt_grid_main")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.lyt_grid_main)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_assign = QtWidgets.QPushButton(self.lyt_grid_main)
        self.btn_assign.setMinimumSize(QtCore.QSize(0, 60))
        self.btn_assign.setObjectName("btn_assign")
        self.gridLayout_2.addWidget(self.btn_assign, 4, 0, 1, 1)
        self.lyt_horizontal_lists = QtWidgets.QHBoxLayout()
        self.lyt_horizontal_lists.setObjectName("lyt_horizontal_lists")
        self.list_geo = QtWidgets.QListWidget(self.lyt_grid_main)
        self.list_geo.setObjectName("list_geo")
        self.lyt_horizontal_lists.addWidget(self.list_geo)
        self.list_mats = QtWidgets.QListWidget(self.lyt_grid_main)
        self.list_mats.setObjectName("list_mats")
        self.lyt_horizontal_lists.addWidget(self.list_mats)
        self.gridLayout_2.addLayout(self.lyt_horizontal_lists, 3, 0, 1, 1)
        self.lyt_horizontal_labels = QtWidgets.QHBoxLayout()
        self.lyt_horizontal_labels.setObjectName("lyt_horizontal_labels")
        self.lbl_geo = QtWidgets.QLabel(self.lyt_grid_main)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_geo.setFont(font)
        self.lbl_geo.setObjectName("lbl_geo")
        self.lyt_horizontal_labels.addWidget(self.lbl_geo)
        self.lbl_mats = QtWidgets.QLabel(self.lyt_grid_main)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_mats.setFont(font)
        self.lbl_mats.setObjectName("lbl_mats")
        self.lyt_horizontal_labels.addWidget(self.lbl_mats)
        self.gridLayout_2.addLayout(self.lyt_horizontal_labels, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.lyt_grid_main)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        window_mats_Isolator.setCentralWidget(self.lyt_grid_main)
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
        self.btn_assign.setText(_translate("window_mats_Isolator", "Assign", None))
        self.lbl_geo.setText(_translate("window_mats_Isolator", "Geometry", None))
        self.lbl_mats.setText(_translate("window_mats_Isolator", "Unassigned materials", None))
        self.pushButton.setText(_translate("window_mats_Isolator", "Reload", None))

