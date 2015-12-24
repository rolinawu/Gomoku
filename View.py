from graphics import *
import math

class Display():

	def __init__(self, w=500,h=700):
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

	def CelltoPoint(self,c):
		if(c % 15 == 0):
			x = 15
		else :
			x = c % 15
		y = math.ceil(c / 15.)
		return Point ((x - 0.5) * self.cellsize, (y - 0.5) * self.cellsize)

	def PointtoCell(self,p):
		if( ( p.getX() / self.cellsize ) == 15):
			x = 1
		else :
			x = ( p.getX() / self.cellsize ) + 1
		cell = ( p.getY() / self.cellsize ) * 15 + x
		return cell

	def DrawPlayer(self, GOb, cell, player='X'):
		''' 
		Parameters: GraphicObject, cell #
		Requires: 1 <= cell <= 225
		Purpose: draw the player on given cell
		'''
		p = self.CelltoPoint(cell)
		playerx = Text(p, player)
		playerx.draw(GOb)

	def existbutton(self, GOb):
		ep2 = Point(self.exitpos.getX()+self.buttonwid, self.exitpos.getY()+self.buttonhei)
		epc = Point((self.exitpos.getX()+ep2.getX())/2,(self.exitpos.getY()+ep2.getY())/2)
		eframe = Rectangle(self.exitpos, ep2)
		eframe.draw(GOb)
		etext = Text (epc, 'Quit')
		etext.draw(GOb)

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