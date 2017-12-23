#Greg Phillips
#12/14/17
#battleship.py

from ggame import* 
from random import randint 

#Dictionary
EMPTY = 0
MISS = 1
HIT = 2
BOAT = 3
RADIUS = 35

def buildBoard():
    board = [[]*5,[]*5,[]*5,[]*5,[]*5]
    return board
    
def redrawAll():
    if data["gameover"] == False:
        for item in App().spritelist[:]:
            item.destroy()
        for row in range(0,5):
            for col in range(0,5):
                Sprite(circle,(RADIUS*2*row+RADIUS, RADIUS*2*col+RADIUS))
        for row in range(0,5):
            for col in range(0,5):
                Sprite(circle,(RADIUS*2*row+RADIUS+400, RADIUS*2*col+RADIUS))        

"""def pickComputerShips():
    pick = False
    if pick == False:
        for i in range(1,4):
            row = randint(0,4)
            col = randint(0,4)
            if data["CompShips"][row][col] != SHIP:
                data["CompShips"][row][col] = SHIP"""

#def computerTurn():


def mouseClick(event):
    if data["gameover"] == False:
        if data["playerShips"] < 3:
            if event.x <= RADIUS*10 and event.y <= RADIUS*10: #only runs if player clicked inside the x coordinates of the game
                roww = event.x//70
                coll = event.y//70
                if data["playerBoard"][roww][coll] != BOAT:
                    data["playerBoard"][roww][coll] = BOAT
                    Sprite(blackCircle, (coll + RADIUS*2, roww + RADIUS*2))
                    data["playerShips"] += 1
    """else:
        roww = event.x//70
        coll = event.y//70"""
        

if __name__ == '__main__': 
    data = {}
    data["gameover"] = False
    data["playerBoard"] = buildBoard()
    data["CompShips"] = buildBoard()
    data["playerShips"] = 0 

    red = Color(0xff0000,1)
    black = Color(0x000000,1)
    blue = Color(0x0000ff,1)

    blackOutline = LineStyle(1,black)

    circle = CircleAsset(RADIUS,blackOutline,blue)
    redCircle = CircleAsset(RADIUS,blackOutline,red)
    blackCircle = CircleAsset(RADIUS,blackOutline,black)

    userText = TextAsset("User Board",fill=black,style="bold 40pt Times") 
    Sprite(userText,(200,700))

    buildBoard()
    #pickComputerShips()
    redrawAll()

    App().listenMouseEvent("click", mouseClick) #Listens for mouse click
    App().run()