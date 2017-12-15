#Greg Phillips
#12/14/17
#battleship.py

from ggame import* 
from random import randint 

EMPTY = 0
MISS = 1

def buildBoard():
    for row in range(0,4):
        for col in range(0,4):
            print(board[row][col],' ',end = '')
        print()
    board = [["a","b","c","d","e"],['f','g','h','i','j'],['k','l','m','n','o']
    printBoard()

    
def redrawAll():

def pickComputerShips():

def computerTurn():
    
def mouseClick():


App().run()