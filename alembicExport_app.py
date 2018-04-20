"""
StandAlone pyqt4

"""
import sys


import platform


from Modules.Qt import QtCore, QtGui, QtWidgets
import Lighting.Maya_lighting_matsIsolator.matsIsolator_UI.mats_Isolator_v01_qt5
reload(Lighting.Maya_lighting_matsIsolator.matsIsolator_UI.mats_Isolator_v01_qt5)
from Lighting.Maya_lighting_matsIsolator.matsIsolator_UI.mats_Isolator_v01_qt5 import Ui_window_mats_Isolator

'''
import Animacion.Maya_Animation_alembicExporter.alembicExport_Core.alembicExportBridge
reload(Animacion.Maya_Animation_alembicExporter.alembicExport_Core.alembicExportBridge)
from Animacion.Maya_Animation_alembicExporter.alembicExport_Core.alembicExportBridge import *#import alembicExportBridge
'''
#Por ventana que hayas disenado

class MyApplication(QtWidgets.QMainWindow, Ui_window_mats_Isolator):

	def __init__(self, parent=None):
		super(MyApplication, self).__init__(parent)
		self.setupUi(self)

if __name__ != "__main__":
	try:
		app = QtWidgets.QApplication(sys.argv)
	except:
		app = QtCore.QCoreApplication.instance()
	window = MyApplication()
	window.setWindowFlags(
		window.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
	#interfaceMacho = alembicExportBridge(window=window)
	window.show()

	try:
		sys.exit(app.exec_())
	except:
		"error al intentar salir"


