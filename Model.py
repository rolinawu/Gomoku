''' 
this is where all the magic(algorithms) happens
'''

class Calc(object):
	def __init__(self):
		self.Xcells = [] 
		self.Ocells = []
		#self.Emptycells = 

	def getXcells(self):
		'''
		Return: the cell numbers of the list of X cells on the board
		'''
		return self.Xcells

	def getOcells(self):
		'''
		Return: the cell numbers of the list of X cells on the board
		'''
		return self.Ocells

	def addXcells(self, cell):
		'''
		Parameter: Int
		Purpose: add the new cell to list Xcells
		'''
		self.Xcells.append(cell)
		print ('adding %d to Xcells' % cell)

	def addOcells(self, cell):
		'''
		Parameter: Int
		Purpose: add the new cell to list Ocells 
		'''
		self.Ocells.append(cell)
		print ('adding %d to Ocells' % cell)
		#self.Ocells += 2**cell

	def cellexist(self, cell):
		'''
		'''
		print ((cell in self.Xcells) or (cell in self.Ocells))
		'''
		'''
		return ((cell in self.Xcells) or (cell in self.Ocells))

	def sumofXcells(self):
		return sum(map(lambda x: 2**x, self.Xcells))

	def sumofOcells(self):
		return sum(map(lambda x: 2**x, self.Ocells))