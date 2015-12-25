

crosses = sum(map(lambda x: 2**x,[110, 125, 112, 129, 140]))
noughts = sum(map(lambda x: 2**x,[95, 126, 142, 143, 113]))
empties = 0
winsList = []
import math

def dependancies(move):
    acc = []
    b = math.floor(move/15)
    for i in range(max(0, move-15*5), min(225, move+15*5)):
        a = move - i
        if (a % 14 == 0 or a % 15 == 0 or a % 16 == 0 or (b == math.floor(i/15) and - 5 < a < 5)):
            acc.append(i)
    return acc

dhashGraph = {}

dlist = map(lambda x: [x, dependancies(x)], range(225))
#__________PREP WORK_______________

#creating all rows
def rows(x):
    if x % 15 < 11:
        return 2**x + 2**(x + 1)+ 2**(x + 2) + 2**(x + 3) + 2**(x + 4)
    else:
        return -1

def diagl(x):
    if x % 15 < 11 and x < 225-(15*4):
        return 2**x + 2**(x + 16)+ 2**(x + 2*16) + 2**(x + 3*16) + 2**(x + 4*16)
    else:
        return -1

def cols(x):
    if x < 225-(15*4):
        return 2**x + 2**(x + 15)+ 2**(x + 2*15) + 2**(x + 3*15) + 2**(x + 4*15)
    else:
        return -1

def diagr(x):
    if 3 < x % 15 and x < 225-(15*4):
        return 2**x + 2**(x + 14)+ 2**(x + 2*14) + 2**(x + 3*14) + 2**(x + 4*14)
    else:
        return -1

def srows(x):
    if x % 15 < 9:
        return [(2**(x + 2) + 2**(x + 3) + 2**(x + 4)), (2**x + 2**(x+6)), (2**(x+1) + 2**(x+5))]
    else:
        return -1

def scols(x):
    if x < 225-(15*6):
        return [(2**(x + 2*15) + 2**(x + 3*15) + 2**(x + 4*15)), 2**x + 2**(x + 6*15), 2**(x + 15) + 2**(x + 5*15)]
    else:
        return -1

def sdiagr(x):
    if x < 225-(15*6) and x % 15 > 5:
        return [(2**(x + 2*14) + 2**(x + 3*14) + 2**(x + 4*14)), 2**x + 2**(x + 6*14), 2**(x + 14) + 2**(x + 5*14)]
    else:
        return -1

def sdiagl(x):
    if x < 225-(15*6) and x % 15 < 9:
        return [(2**(x + 2*16) + 2**(x + 3*16) + 2**(x + 4*16)), 2**x + 2**(x + 6*16), 2**(x + 16) + 2**(x + 5*16)]
    else:
        return -1

def brows(x):
    if x % 15 < 10:
        return [(2**(x + 1) + 2**(x + 2) + 2**(x + 3) + 2**(x + 4)), (2**x + 2**(x+5))]
    else:
        return -1

def bcols(x):
    if x < 225 - 15*5:
        return [(2**(x + 15) + 2**(x + 2*15) + 2**(x + 45) + 2**(x + 60)), (2**x + 2**(x+75))]
    else:
        return -1

def bdiagl(x):
    if x % 15 < 10 and 225 - 15*5 > x:
        return [(2**(x + 16) + 2**(x + 32) + 2**(x + 48) + 2**(x + 16*4)), (2**x + 2**(x+16*5))]
    else:
        return -1

def bdiagr(x):
    if x % 15 > 4 and 225 - 15*5 > x:
        return [(2**(x + 14) + 2**(x + 28) + 2**(x + 42) + 2**(x + 14*4)), (2**x + 2**(x+5*14))]
    else:
        return -1

#turning them into lists

fRows = [rows(x) for x in range(225)] + [cols(x) for x in range(225)] + [diagl(x) for x in range(225)] + [diagr(x) for x in range(225)]

sRows = [srows(x) for x in range(225)] + [scols(x) for x in range(225)] + [sdiagl(x) for x in range(225)] + [sdiagr(x) for x in range(225)]

xRows = [brows(x) for x in range(225)] + [bcols(x) for x in range(225)] + [bdiagl(x) for x in range(225)] + [bdiagr(x) for x in range(225)]

xRows = filter (lambda z: z != -1, xRows)

fRows = filter (lambda x: x != -1, fRows)

sRows = filter (lambda x: x != -1, sRows)

#creating the hashes

fhashGraph = {}

shashGraph = {}

xhashGraph = {}

def finder(x, lst):
    return filter (lambda y: x & y != 0, lst)

def finder2(x, lst):
    return filter (lambda y: x & (y[0] + y[1]) != 0, lst)

def finder3(x, lst):
    return filter (lambda z: x & z[0] != 0, lst)

fgraph = map (lambda x: [2**x, finder(2**x, fRows)], range(225))
sgraph = map (lambda x: [2**x, finder2(2**x, sRows)], range(225))
xgraph = map (lambda x: [2**x, finder3(2**x, xRows)], range(225))


def makeHash(hash, graph):
    for x in graph:
        hash[x[0]] = x[1]

def checkThreat(move, person, oppo):
    checker = person + move
    priority = 0;
    gg = -1
    for x in fhashGraph[move]:
        check = checker & x
        if check == x:
            return [0, 5]
        elif bin(check).count("1") == 4 and (x - check) & oppo == 0:
            return [x - check, 4]
    for y in shashGraph[move]:
        inner = checker & y[0]
        outer = oppo & y[1]
        mid = (checker + oppo) & y[2]
        if (inner == y[0] and mid == 0):
            if (outer == 0):
                return [y[2], 3]
            elif (outer < y[1]):
                return [y[1] + y[2] - outer, 3]
    for z in xhashGraph[move]:
        inner = checker & z[0]
        outer = oppo & (z[1] + z[0])
        if outer == 0 and bin(inner).count("1") == 3:
            return [z[1] + z[0] - inner, 3]
    return [gg, 0]

def checkThreatfour(move, person, oppo):
    checker = person + move
    priority = 0;
    gg = [-1, 0]
    for x in fhashGraph[move]:
        check = checker & x
        if check == x:
            return [0, 5]
        elif bin(check).count("1") == 4 and (x - check) & oppo == 0:
            return [x - check, 4]
    return gg

makeHash(fhashGraph, fgraph)

makeHash(shashGraph, sgraph)

makeHash(dhashGraph, dlist)

makeHash(xhashGraph, xgraph)

#-----
#takes in 2 numbers and returns a boolean as to whether the position has a forced win or not
'''
def checkline(line):
    priority = line[1]
    first = line[3]
    second = line[2]
    for i in moves:
        if (first + second) & 2**i == 0:
            threat = checkThreat(2**i, first, second)
            if threat[1] == 5:
                return False
            
            if threat[1] > priority:
                bob = ThreatSearch(second + threat[0], first + 2**i, 1, [], range(225))
                if bob == []:
                    return False
    return True
'''
def checkline(line, sp, fp):
    if not line:
        return True
    myThreat = checkThreat(2**line[0][0], fp, sp)
    if myThreat[0] == -1:
        return False
    fp = fp + 2**line[0][0]
    for i in range(225):
        opThreat = checkThreatfour(2**i, sp, fp)
        if opThreat[1] == 5:
            return False
        elif opThreat[1] > myThreat[1]:
            bob = checkline(line, fp + opThreat[0] - 2**line[0][0], sp + 2**i)
            if bob != True:
                return True
    return checkline(line[1:], fp, sp + myThreat[0])

'''
takes in a bit with all the moves of the first player, a bit with all the moves of the second player,
the current depth, starting at 0, the accumulater, starting at [], and range(225). Check how I called it below.
'''
def ThreatSearch(first, second, depth, acc, moves):
    empty = first + second
    global winsList
    for i in moves:
        move = 2**i
        if move & empty == 0:
            threat = checkThreat(move, first, second)
            if threat[0] == 0:
                jj = checkline(acc, crosses, noughts)
                if jj:
                   winsList = winsList + [map(lambda x: x[0], acc) + [i]]
        
            elif threat[0] > 0:
                ac2 = acc + [[i, threat, first, second]]
                nextMoves = dhashGraph[i]
                ThreatSearch(first + move, second + threat[0], depth + 1, ac2, nextMoves)
#Takes in a position, returns a list of threats

#print dhashGraph
#print fhashGraph[2**3]
#print shashGraph[2**3]
#print xhashGraph[2**3]
#print crosses
#ThreatSearch(noughts, crosses, 0, [], range(225))
#print winsList
#print checkThreat(2**111, noughts, crosses)
#print xhashGraph[2**111]
#print bdiagl(79)


