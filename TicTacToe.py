from View import *
from Model import *
from Control import *
from graphics import *
import script
import tkMessageBox


def main():
	loopc = 1
	view = Display()
	control = Control()
	model = Calc()
	script
	GOb = GraphWin("TicTacToe", view.getWinWid(), view.getWinHei())
	#control.GameStart(GOb)
	#### for testing use only ####
	for i in range(226):
		view.DrawPlayer(GOb, i, str(i), color_rgb(200,200,200))

	crosses = [110, 125, 112, 129, 140]
	noughts = [95, 126, 142, 143, 113]

	model.Xcells = crosses
	model.Ocells = noughts

	for x in crosses:
			view.DrawPlayer(GOb, x, 'X')
	for o in noughts:
			view.DrawPlayer(GOb, o, 'O')

	#### for testing use only ####
	view.board(GOb)
	view.createbutton(GOb, view.anapos, 'Analyze')
	view.createbutton(GOb, view.exitpos,'Quit')
	while control.gamestat == False: 
		mpos = GOb.getMouse()
		mstate = control.CheckMousePos(mpos)
		while model.cellexist(mstate):
			mpos = GOb.getMouse()
			mstate = control.CheckMousePos(mpos) 
		# call function that calculates the next best move
		####control.State(GOb)
		loopc += 1
		if mstate == 'Exit':
			GOb.close()
			break
		elif mstate == False:
			print 'you are off the grid'
			#return 
		elif mstate == 'Analyze':
			#print model.sumofXcells()
			#print sum(map(lambda x: 2**x,[110, 125, 112, 129, 140]))
			script.ThreatSearch(model.sumofOcells(), model.sumofXcells(), 0, [], range(225))
			#print script.winsList
			winsoln = []
			for i in script.winsList:
				winsoln.append(str(i))
			tkMessageBox.showinfo(title="All solutions", message= str('\n'.join(winsoln)))
			# view.Console(GOb, Point(view.width+150, 10), str(script.ThreatSearch(crosses, noughts, 0, [], range(225))))
		elif (loopc % 2) == 0:
			#mstate gives the cell #
			model.addXcells(mstate)
			view.DrawPlayer(GOb, mstate, 'X')
		else:
			model.addOcells(mstate)
			view.DrawPlayer(GOb, mstate, 'O')
			#add the cell to the number that keeps track of all O cells
			#the cell will be drawn next time we call Control.State()

	GOb.close() #only gets to here when game ended


if __name__ == '__main__':
	main()
