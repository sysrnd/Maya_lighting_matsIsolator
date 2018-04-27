# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Z:\RnD\Pipeline\Maya\Scripts\Lighting\Maya_lighting_matsIsolator\matsIsolator_UI\resources\mats_Isolator_v01.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_window_mats_Isolator(object):
    def setupUi(self, window_mats_Isolator):
        window_mats_Isolator.setObjectName(_fromUtf8("window_mats_Isolator"))
        window_mats_Isolator.resize(545, 671)
        self.lyt_grid_main = QtGui.QWidget(window_mats_Isolator)
        self.lyt_grid_main.setObjectName(_fromUtf8("lyt_grid_main"))
        self.gridLayout_2 = QtGui.QGridLayout(self.lyt_grid_main)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.btn_assign = QtGui.QPushButton(self.lyt_grid_main)
        self.btn_assign.setMinimumSize(QtCore.QSize(0, 60))
        self.btn_assign.setObjectName(_fromUtf8("btn_assign"))
        self.gridLayout_2.addWidget(self.btn_assign, 4, 0, 1, 1)
        self.lyt_horizontal_lists = QtGui.QHBoxLayout()
        self.lyt_horizontal_lists.setObjectName(_fromUtf8("lyt_horizontal_lists"))
        self.list_geo = QtGui.QListWidget(self.lyt_grid_main)
        self.list_geo.setObjectName(_fromUtf8("list_geo"))
        self.lyt_horizontal_lists.addWidget(self.list_geo)
        self.list_mats = QtGui.QListWidget(self.lyt_grid_main)
        self.list_mats.setObjectName(_fromUtf8("list_mats"))
        self.lyt_horizontal_lists.addWidget(self.list_mats)
        self.gridLayout_2.addLayout(self.lyt_horizontal_lists, 3, 0, 1, 1)
        self.lyt_horizontal_labels = QtGui.QHBoxLayout()
        self.lyt_horizontal_labels.setObjectName(_fromUtf8("lyt_horizontal_labels"))
        self.lbl_geo = QtGui.QLabel(self.lyt_grid_main)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_geo.setFont(font)
        self.lbl_geo.setObjectName(_fromUtf8("lbl_geo"))
        self.lyt_horizontal_labels.addWidget(self.lbl_geo)
        self.lbl_mats = QtGui.QLabel(self.lyt_grid_main)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_mats.setFont(font)
        self.lbl_mats.setObjectName(_fromUtf8("lbl_mats"))
        self.lyt_horizontal_labels.addWidget(self.lbl_mats)
        self.gridLayout_2.addLayout(self.lyt_horizontal_labels, 2, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton = QtGui.QPushButton(self.lyt_grid_main)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        window_mats_Isolator.setCentralWidget(self.lyt_grid_main)
        self.menubar = QtGui.QMenuBar(window_mats_Isolator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 545, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        window_mats_Isolator.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(window_mats_Isolator)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        window_mats_Isolator.setStatusBar(self.statusbar)

        self.retranslateUi(window_mats_Isolator)
        QtCore.QMetaObject.connectSlotsByName(window_mats_Isolator)

    def retranslateUi(self, window_mats_Isolator):
        window_mats_Isolator.setWindowTitle(_translate("window_mats_Isolator", "Materials Isolator", None))
        self.btn_assign.setText(_translate("window_mats_Isolator", "Assign", None))
        self.lbl_geo.setText(_translate("window_mats_Isolator", "Geometry", None))
        self.lbl_mats.setText(_translate("window_mats_Isolator", "Unassigned materials", None))
        self.pushButton.setText(_translate("window_mats_Isolator", "Reload", None))

