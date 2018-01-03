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
    board = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    return board
    
def redrawAll():
    if data["gameover"] == False:
        for item in App().spritelist[:]:
            item.destroy()
        userText = TextAsset("Player",fill=black,style="bold 40pt Times") 
        Sprite(userText, (110,375))
        computerText = TextAsset("Computer",fill=black,style="bold 40pt Times") 
        Sprite(computerText, (465,375))
        for row in range(0,5):
            for col in range(0,5):
                Sprite(circle,(RADIUS*2*row+RADIUS, RADIUS*2*col+RADIUS))
        for row in range(0,5):
            for col in range(0,5):
                Sprite(circle,(RADIUS*2*row+RADIUS+400, RADIUS*2*col+RADIUS))        

def pickComputerShips():
    pick = False
    if pick == False:
        for i in range(1,4):
            row = randint(0,4)
            col = randint(0,4)
            if data["CompShips"][row][col] != BOAT:
                data["CompShips"][row][col] = BOAT

#def computerTurn():


def mouseClick(event):
    if data["gameover"] == False:
        if data["playerShips"] < 3:
            if event.x <= RADIUS*10 and event.y <= RADIUS*10: #only runs if player clicked inside the x coordinates of the game
                roww = event.y//70
                coll = event.x//70
                if data["userBoard"][roww][coll] != BOAT:
                    data["userBoard"][roww][coll] = BOAT
                    Sprite(blackCircle, (RADIUS+2*coll*RADIUS, RADIUS+2*roww*RADIUS))
                    data["playerShips"] += 1
        else:
            if event.x <= (RADIUS*10)+400 and event.x >= (RADIUS*10)+50 and event.y <= RADIUS*10: #only runs if player clicked inside the x coordinates of the game
                roww = (event.x-400)//70
                coll = event.y//70
                if data["ComputerBoard"][roww][coll] != BOAT:
                    data["ComputerBoard"][roww][coll] = MISS
                    Sprite(whiteCircle, ((RADIUS+2*roww*RADIUS)+400, RADIUS+2*coll*RADIUS))
                else:
                    data["ComputerBoard"][roww][coll] = BOAT:
                        data["ComputerBoard"][roww][coll] = HIT
                        Sprite(redCircle, ((RADIUS+2*roww*RADIUS)+400, RADIUS+2*coll*RADIUS))
                        
        

if __name__ == '__main__': 
    data = {}
    data["gameover"] = False
    data["userBoard"] = buildBoard()
    data["CompShips"] = buildBoard()
    data["ComputerBoard"] = buildBoard()
    data["playerShips"] = 0 

    red = Color(0xff0000,1)
    black = Color(0x000000,1)
    blue = Color(0x0000ff,1)
    white = Color(0xffffff,1)

    blackOutline = LineStyle(1,black)

    circle = CircleAsset(RADIUS,blackOutline,blue)
    redCircle = CircleAsset(RADIUS,blackOutline,red)
    blackCircle = CircleAsset(RADIUS,blackOutline,black)
    whiteCircle = CircleAsset(RADIUS,blackOutline,white)

   

    buildBoard()
    pickComputerShips()
    redrawAll()

    App().listenMouseEvent("click", mouseClick) #Listens for mouse click
    App().run()