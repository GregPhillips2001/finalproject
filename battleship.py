#Greg Phillips
#12/14/17
#battleship.py

from ggame import* 
from random import randint 

#Dictionary
EMPTY = 0
MISS = 1
HIT = 2
RADIUS = 40

def buildBoard():
    board = [[]*5,[]*5,[]*5,[]*5,[]*5]
    return board
    
def redrawAll():
    for item in App().spritelist[:]:
        item.destroy()
    for row in range(0,5):
        for col in range(0,5):
            Sprite(circle,(RADIUS+5*row, RADIUS+5*col))
            

#def pickComputerShips():
    

#def computerTurn():
    
    
#def mouseClick():
    
    
if __name__ == '__main__': 
    
    data = {}
    
    red = Color(0xff0000,1)
    black = Color(0x000000,1)
    blue = Color(0x0000ff,1)
    
    blackOutline = LineStyle(1,black)
    
    circle = CircleAsset(RADIUS,blackOutline,blue)
    redCircle = CircleAsset(RADIUS,blackOutline,red)
    
    buildBoard()
    redrawAll()

    App().run()