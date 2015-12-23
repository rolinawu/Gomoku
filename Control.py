'''
import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__),'..'))

import Game.View
import Game.Model
'''
from View import *

class Control(object):

	def __init__(self):
		self.gamestat = False
		self.view = Display()

	def GameStart(self, GOb):
		self.view.board(GOb)
		#View.drawPlayer(GOb, 113)
		'''
		drawPlayer(GOb, 1)
		drawPlayer(GOb, 3, 'O')
		drawPlayer(GOb, 14, 'X')
		drawPlayer(GOb, 15, 'X')
		drawPlayer(GOb, 225, 'O')
		'''
		self.view.existbutton(GOb)

	def getGameStatus(self):
		return self.gamestat

	def State(self, GOb):
		self.view.board(GOb)
		#draw all the cells 
		self.view.existbutton(GOb)

	def CheckMousePos(self, mpos):
		'''
		Return: 'Exit'-if mouse hits exist button, Cell number if mouse hits an cell, False if no change made due to mouse click
		''' 
		if (mpos.getX() > self.view.getexitpos().getX()):
			if (mpos.getX() < (self.view.getexitpos().getX() + self.view.getbuttonwid())):
				if (mpos.getY() > self.view.getexitpos().getY()):
					if  (mpos.getY() < (self.view.getexitpos().getY()+self.view.getbuttonhei())):
						return 'Exit'
		if (mpos.getX() > self.view.getgridtopleftpt().getX()):
			if (mpos.getX() < (self.view.getgridbutrightpt().getX() + self.view.getbuttonwid())):
				if (mpos.getY() > self.view.getgridtopleftpt.getY()):
					if  (mpos.getY() < (self.view.getgridtopleftpt.getY()+self.view.getbuttonhei())):
						return self.view.PointtoCell(mpos)

