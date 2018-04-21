import maya.cmds as cmds

class matsCore(object):

	def __init__(self):
		self.invalidMats = ['lambert1']

	def main(self):
		emptyMats_, emptySGs_ = self.scanUnassignedMats()

	def scanUnassignedMats(self):
		'''
		returns two lists, one with the mats and one with SGs
		'''

		emptyMats = []
		emptySGs = []
		for shading in cmds.ls(et='shadingEngine'):
			conn = cmds.sets(shading, q=True)
			if conn == None:
				matConn = cmds.listConnections(shading + '.surfaceShader')[0]
				if matConn not in emptyMats and matConn not in self.invalidMats:
					emptyMats.append(str(matConn))
					emptySGs.append(str(shading))

		
		return emptyMats, emptySGs

	def assignMat(self):
		pass

	def getSel(self):
		sel = cmds.ls(sl=True)

		return sel