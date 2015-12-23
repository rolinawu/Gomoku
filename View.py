from graphics import *
import math

class Display():
	
	width = None
	height = None
	cellsize = 0
	buttonwid = None
	buttonhei = None
	exitpos = None
	gridtopleftpt = None
	gridbutrightpt = None
	

	def __init___(self, w=500,h=700):
		self.width = w #window width
		self.height = h #window height
		self.cellsize = (self.width - 3)/15
		self.gridtopleftpt = Point(3,3)
		self.gridbutrightpt = Point(self.width,self.width)
		self.buttonwid = 80 #width of all buttons 
		self.buttonhei = 30 #height of all buttons
		#coordinate of exit button
		self.exitpos = Point(self.width/100, self.height - 2 * self.buttonhei)		

	def board(self, GOb):
		''' 
		Parameters: GraphicObject
		Purpose: draw the grid
		'''
		for i in range(16):
			s = i * self.cellsize
			l = self.width
			hline = Line(Point(0, s+3),Point(l, s+3))
			vline = Line(Point(s+3, 0), Point(s+3, l))
			hline.draw(GOb)
			vline.draw(GOb)

	def getWinWid(self):
		return self.width

	def getWinHei(self):
		return self.height

	def getbuttonwid(self):
		return self.buttonwid

	def getbuttonhei(self):
		return self.buttonhei
		
	def getexitpos(self):
		return self.exitpos	

	def getgridtopleftpt(self):
		return self.gridtopleftpt

	def getgridbutrightpt(self):
		return self.gridbutrightpt

	def drawPlayer(self, GOb, cell, player='X'):
		''' 
		Parameters: GraphicObject, cell #
		Requires: 1 <= cell <= 225
		Purpose: draw the player on given cell
		'''
		p = CelltoPoint(cell)
		playerx = Text(p, player)
		playerx.draw(GOb)

	def CelltoPoint(self,c):
		if(cell % 15 == 0):
			x = 15
		else :
			x = cell % 15
		y = math.ceil(cell / 15.)
		return Point ((x - 0.5) * self.cellsize, (y - 0.5) * self.cellsize)

	def PointtoCell(self,p):
		'''
		place holder
		'''
		## something
		#toooooo tired to think of this anymore zzzzzzzzzzzzzzz
		return

	def existbutton(self, GOb):
		ep2 = Point(self.exitpos.getX()+buttonwid, self.exitpos.getY()+buttonhei)
		epc = Point((self.exitpos.getX()+ep2.getX())/2,(self.exitpos.getY()+ep2.getY())/2)
		eframe = Rectangle(exitpos, ep2)
		eframe.draw(GOb)
		etext = Text (epc, 'Quit')
		etext.draw(GOb)

def main():
	view = Display()
	GOb = GraphWin("TicTacToe", view.getWinWid(), view.getWinHei())
	view.board(GOb)
	#View.drawPlayer(GOb, 113)
	view.drawPlayer(GOb, 1)
	view.drawPlayer(GOb, 3, 'O')
	view.drawPlayer(GOb, 14, 'X')
	view.drawPlayer(GOb, 15, 'X')
	view.drawPlayer(GOb, 225, 'O')
	view.existbutton(GOb)
main()

'''
def drawX(GOb, x, y):
###
Parameters: GraphicObject, x-coord, y-coord
Requires: 1 <= x, y <= 15
Purpose: draw a 'X' on given position
###
	p = Point ((3 + (x - 0.5) * (width - 3)/15), (3 + (y - 0.5) * (width - 3)/15))
	playerx = Text(p, 'X')
	playerx.draw(GOb)

def drawO(GOb, x, y):
###
Parameters: GraphicObject, x-coord, y-coord
Requires: 1 <= x, y <= 15
Purpose: draw a 'O' on given position
###
	p = Point ((3 + (x - 0.5) * (width - 3)/15), (3 + (y - 0.5) * (width - 3)/15))
	playero = Text(p, 'O')
	playero.draw(GOb)
'''