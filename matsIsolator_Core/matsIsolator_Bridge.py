import maya.cmds as cmds
from Modules.Qt import QtCore, QtGui, QtWidgets

import Lighting.Maya_lighting_matsIsolator.matsIsolator_Core.mats_core
reload(Lighting.Maya_lighting_matsIsolator.matsIsolator_Core.mats_core)
from Lighting.Maya_lighting_matsIsolator.matsIsolator_Core.mats_core import matsCore

class MatsIsolatorBridge(object):
	def __init__(self, window):

		'''
		'''
		self.window = window

		self.window.list_geo.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)

		self.window.btn_reload.clicked.connect(self.populateUI)
		self.window.btn_assign.clicked.connect(self.assignMat)
		self.populateUI()

	def populateUI(self):
		
		if self.window.list_mats.count() > 0:
			self.window.list_mats.clear()

		if self.window.list_geo.count() > 0:
			self.window.list_geo.clear()

		self.core = matsCore()
		self.mats, self.sgs = self.core.scanUnassignedMats()
		self.geo = self.core.scanUnassignedGeo()

		for mat in self.sgs:
			self.window.list_mats.addItem(str(mat))

		for geo in self.geo:
			self.window.list_geo.addItem(str(geo))

	def assignMat(self):
		activeMat = self.window.list_mats.selectedItems()[0]
		activeGeo = self.window.list_geo.selectedItems()

		print activeMat.text()
		for geo in activeGeo:

			geo = geo.text()
			activeMat = activeMat.text()

			self.core.assignMat(geo, activeMat)


