from graphics import *
import math

class Display():

	def __init__(self, w=500,h=600):
		self.width = w #window width
		self.height = h #window height
		self.cellsize = (self.width - 3)/15
		self.gridtopleftpt = Point(3,3)
		self.gridbutrightpt = Point(self.width,self.width)
		self.buttonwid = 80 #width of all buttons 
		self.buttonhei = 30 #height of all buttons
		#coordinate of exit button
		self.bdis = 20 #the distance between each buttons
		self.exitpos = Point(self.width - self.buttonwid - self.bdis, self.height - 2 * self.buttonhei)	
		self.resetpos = Point(self.exitpos.getX() - self.buttonwid - self.bdis, self.exitpos.getY())	
		self.anapos = Point(self.exitpos.getX() - 2*self.buttonwid - 2*self.bdis, self.exitpos.getY())	

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
		if((c % 15) == 0):
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

	def DrawPlayer(self, GOb, cell, player='X', color = color_rgb(0,0,0)):
		''' 
		Parameters: GraphicObject, cell #
		Requires: 1 <= cell <= 225
		Purpose: draw the player on given cell
		'''
		p = self.CelltoPoint(cell)
		player = Text(p, player)
		player.setTextColor(color)
		player.draw(GOb)

	def Console(self, GOb, p, text='Console:', color = color_rgb(0,0,0)):
		''' 
		Parameters: GraphicObject, cell #
		Requires: 1 <= cell <= 225
		Purpose: draw the player on given cell
		'''
		display = Text(p, text)
		display.setTextColor(color)
		display.draw(GOb)

	def createbutton(self, GOb, pos = None, text = 'Quite'):
		if pos is None:
			pos = self.exitpos
		ep2 = Point(pos.getX()+self.buttonwid, pos.getY()+self.buttonhei)
		epc = Point((pos.getX()+ep2.getX())/2,(pos.getY()+ep2.getY())/2)
		eframe = Rectangle(pos, ep2)
		eframe.draw(GOb)
		etext = Text (epc, text)
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