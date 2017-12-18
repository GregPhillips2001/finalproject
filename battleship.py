#Greg Phillips
#12/14/17
#battleship.py

from ggame import* 
from random import randint 

EMPTY = 0
MISS = 1
HIT = 2
RADIUS = 50

def buildBoard():
    board = []
    for row in range(0,2):
        for col in range(0,4):
            sprite(circle,(row,col))
            """sprite(board[row][col],' ',end = '')#what does this do"""
        return board
    board = [[]*5,[]*5,[]*5,[]*5,[]*5]
    printBoard()

    
def redrawAll():

def pickComputerShips():

def computerTurn():
    
def mouseClick():
    
if __name__ == '__main__': 
    
    data = {}
    
    red = Color(0xff0000,1)
    black = Color(0x000000,1)
    
    circle = CircleAsset(RADIUS,blackOutline)
    
    buildBoard()


App().run()