import maya.cmds as cmds

class matsCore(object):

	def __init__(self):

		self.invalidMats = ['lambert1']

	def main(self):
		pass
		#emptyMats_, emptySGs_ = self.scanUnassignedMats()

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

	def scanUnassignedGeo(self):

		blankGeo = []
		for geo in cmds.ls(et='mesh'):
			if cmds.listConnections(geo + '.instObjGroups')[0] == 'initialShadingGroup':
				geoParent = cmds.listRelatives(geo, p=True)[0]
				blankGeo.append(geoParent)

		return blankGeo

	def assignMat(self, geoParent, mat):

		geo = cmds.listRelatives(geoParent, s=True)[0]
		#mat = 
		cmds.sets(geo, e=True, fe=mat)

		
		

