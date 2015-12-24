from View import *
from Model import *
from Control import *
from graphics import *

def main():
	view = Display()
	control = Control()
	model = Calc()
	GOb = GraphWin("TicTacToe", view.getWinWid(), view.getWinHei())
	control.GameStart(GOb)
	while control.gamestat == False:
		# call function that calculates the next best move
		control.State(GOb)
		mpos = GOb.getMouse()
		mstate = control.CheckMousePos(mpos) 
		if mstate == 'Exit':
			GOb.close()
			break
		elif mstate == False:
			print 'you are off the grid'
			#return  
		else:
			cell = view.PointtoCell(mstate)
			model.addOcells(cell)
			view.DrawPlayer(GOb, mstate, 'O')
			#add the cell to the number that keeps track of all O cells
			#the cell will be drawn next time we call Control.State()

	GOb.close() #only gets to here when game ended


if __name__ == '__main__':
	main()
