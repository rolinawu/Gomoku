'''
import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__),'..'))

import Game.View
import Game.Model
'''
import sys
from View import *
from Model import *

class Control(object):

	def __init__(self):
		self.gamestat = False
		self.view = Display()
		self.model = Calc()

	def GameStart(self, GOb):
		self.view.board(GOb)
		self.view.DrawPlayer(GOb, 113)
		'''
		drawPlayer(GOb, 1)
		drawPlayer(GOb, 3, 'O')
		drawPlayer(GOb, 14, 'X')
		drawPlayer(GOb, 15, 'X')
		drawPlayer(GOb, 225, 'O')
		'''
		self.view.createbutton(GOb)
	'''
	def State(self, GOb):
		self.view.board(GOb)
		crosses = self.model.getXcells()
		noughts = self.model.getOcells()
		for x in crosses:
			self.view.DrawPlayer(GOb, x, 'X')
		for o in noughts:
			self.view.DrawPlayer(GOb, o, 'O')
		#draw all the cells 
	'''


	def check_within_bounds(self, x, y, left_bound, right_bound, top_bound, bottom_bound):
		#sys.stderr.write("Checking if (%.2f, %.2f) is within (%d,%d,%d,%d)..."%(x, y, left_bound,right_bound,top_bound,bottom_bound))
		within_bounds = (x <= right_bound) and (x >= left_bound) and (y <= bottom_bound) and (y >= top_bound)
		return within_bounds

	def CheckMousePos(self, mpos):
		'''
		Return: 'Exit'-if mouse hits exist button, Cell number if mouse hits an cell, False if no change made due to mouse click
		''' 
		
		if self.check_within_bounds(x = mpos.getX(), y = mpos.getY(), 
			left_bound = self.view.exitpos.getX(), 
			right_bound = self.view.exitpos.getX() + self.view.buttonwid,
			top_bound = self.view.exitpos.getY(),
			bottom_bound = self.view.exitpos.getY()+self.view.buttonhei):
			return 'Exit'
		if self.check_within_bounds(x = mpos.getX(), y = mpos.getY(), 
			left_bound = self.view.anapos.getX(), 
			right_bound = self.view.anapos.getX() + self.view.buttonwid,
			top_bound = self.view.anapos.getY(),
			bottom_bound = self.view.anapos.getY()+self.view.buttonhei):
			return 'Analyze'
		if self.check_within_bounds(x = mpos.getX(), y = mpos.getY(),
			left_bound = self.view.gridtopleftpt.getX(),
			right_bound = self.view.gridbutrightpt.getX(),
			top_bound = self.view.gridtopleftpt.getY(),
			bottom_bound = self.view.gridbutrightpt.getY()):
			#print('you are on the grid')
			return self.view.PointtoCell(mpos)
		else:
			return False

