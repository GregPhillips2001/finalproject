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

def buildBoard(): #creates a 5x5 empty matrix 
    board = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    return board
    
def redrawAll(): #creates the board 
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
    if data["gameover"] == False:
        #plaves three boats in random places on the computer board 
        i = 0
        while i<3:
            row = randint(0,4)
            col = randint(0,4)
            if data["ComputerBoard"][row][col] != BOAT: #only places the boat if there isnt one there already
                data["ComputerBoard"][row][col] = BOAT
                i += 1 #keeps track of how many boats are placed 

def computerTurn():  
    if data["gameover"] == False:
        #computer randomly picks a spot to see if there is a boat
        row = randint(0,4)
        col = randint(0,4)
        if data["userBoard"][row][col] != MISS and data["userBoard"][row][col] != HIT: #only counts the move if the computer hasnt guessed there already
            if data["userBoard"][row][col] != BOAT: #if there is no boat it is marked as a boat
                data["userBoard"][row][col] = MISS
                Sprite(whiteCircle, ((RADIUS+2*row*RADIUS), RADIUS+2*col*RADIUS))
            else:
                data["userBoard"][row][col] = HIT #if there is a boat it is marked as a hit
                Sprite(redCircle, ((RADIUS+2*row*RADIUS), RADIUS+2*col*RADIUS))
                data["comphits"] += 1 #keeps track of how many boats the computer has hit
                if data["comphits"] == 3: #once all boats are hit the game is over 
                    data["gameover"] = True
                    computerwin = TextAsset("Computer Wins",fill=black,style="bold 80pt Times") 
                    Sprite(computerwin, (180,100))
                    
        else:
            computerTurn() #if the boats randomly generate place has already been chosen it reruns this part of the program

def mouseClick(event):
    if data["gameover"] == False:
        #places boats on players board until 3 are placed
        if data["playerShips"] < 3:
            if event.x <= RADIUS*10 and event.y <= RADIUS*10: #only runs if player clicked inside the x coordinates of the game
                roww = event.y//70
                coll = event.x//70
                if data["userBoard"][coll][roww] != BOAT: #prevents you from placing a boat where one already is 
                    data["userBoard"][coll][roww] = BOAT
                    Sprite(blackCircle, (RADIUS+2*coll*RADIUS, RADIUS+2*roww*RADIUS))
                    data["playerShips"] += 1 #keeps track of how many boats are placed 
        else:
            #players guess on computer board for where one of the boats is 
            if event.x <= (RADIUS*10)+400 and event.x >= (RADIUS*10)+50 and event.y <= RADIUS*10: #only runs if player clicked inside the x coordinates of the game
                roww = (event.x-400)//70
                coll = event.y//70
                #if there is no boat then it is marked as a miss
                if data["ComputerBoard"][roww][coll] != BOAT:
                    data["ComputerBoard"][roww][coll] = MISS
                    Sprite(whiteCircle, ((RADIUS+2*roww*RADIUS)+400, RADIUS+2*coll*RADIUS))
                else: #if there is a boat there it is marked as a hit
                    data["userBoard"][roww][coll] = HIT
                    Sprite(redCircle, ((RADIUS+2*roww*RADIUS)+400, RADIUS+2*coll*RADIUS))
                    data["playerhits"] += 1
                    if data["playerhits"] == 3: #sees if all the boats have been hit
                        data["gameover"] = True
                        playerwin = TextAsset("Player Wins",fill=black,style="bold 80pt Times") 
                        Sprite(playerwin, (240,100))
                computerTurn() #makes it so that after you click trying to hit their boat it is the computer turn

if __name__ == '__main__': #this part of the program sets up the game 
    #dictionary
    data = {}
    data["gameover"] = False
    data["userBoard"] = buildBoard()
    data["ComputerBoard"] = buildBoard()
    data["playerShips"] = 0 
    data["playerhits"] = 0
    data["comphits"] = 0

    #colors
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