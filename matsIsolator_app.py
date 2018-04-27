"""
StandAlone pyqt4

"""
import sys


import platform


from Modules.Qt import QtCore, QtGui, QtWidgets


import Lighting.Maya_lighting_matsIsolator.matsIsolator_UI.mats_Isolator_v01_qt5
reload(Lighting.Maya_lighting_matsIsolator.matsIsolator_UI.mats_Isolator_v01_qt5)
from Lighting.Maya_lighting_matsIsolator.matsIsolator_UI.mats_Isolator_v01_qt5 import Ui_window_mats_Isolator


import Lighting.Maya_lighting_matsIsolator.matsIsolator_Core.matsIsolator_Bridge
reload(Lighting.Maya_lighting_matsIsolator.matsIsolator_Core.matsIsolator_Bridge)
from Lighting.Maya_lighting_matsIsolator.matsIsolator_Core.matsIsolator_Bridge import MatsIsolatorBridge

#Por ventana que hayas disenado

class MyApplication(QtWidgets.QMainWindow, Ui_window_mats_Isolator):

    def __init__(self, parent=None):
        super(MyApplication, self).__init__(parent)
        self.setupUi(self)

if __name__ != "__main__":
    """
    try:
        app = QtWidgets.QApplication(sys.argv)
    except:
        app = QtCore.QCoreApplication.instance()
    """
    if QtCore.QCoreApplication.instance() is not None:
        app = QtCore.QCoreApplication.instance()
    else:
        app = QtWidgets.QApplication(sys.argv)

    app.aboutToQuit.connect(app.quit)

    window = MyApplication()
    window.setWindowFlags(
        window.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
    interfaceMacho = MatsIsolatorBridge(window=window)
    window.show()
    try:
        sys.exit(app.exec_())
    except:
        "error al intentar salir"