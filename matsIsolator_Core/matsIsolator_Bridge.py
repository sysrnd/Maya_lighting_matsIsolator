from Modules.Qt import QtCore, QtGui, QtWidgets

import Lighting.Maya_lighting_matsIsolator.matsIsolator_Core.mats_core
reload(Lighting.Maya_lighting_matsIsolator.matsIsolator_Core.mats_core)
from Lighting.Maya_lighting_matsIsolator.matsIsolator_Core.mats_core import *

class MatsIsolatorBridge(object):
	def __init__(self, window):

		'''
		'''
		self.window = window

	def populateUI(self):
		
		pass