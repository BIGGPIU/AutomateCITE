from random import randint
import keyboard
from time import sleep
import copy
from requests import post
from requests import get 
from senseHAT import senseHAT
from datetime import datetime

colordict = {
    1:(255,0,0),
    2:(0,0,255),
    3:(0,255,0),
    "#":(255, 196, 0)
}

# 0 = empty
# 1 = obstacle
# 2 = playerSpawn
# 3 = exit
mazes = {
    "Normal":[
        [
            [1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1],
            [0,0,0,0,0,0,0,0],
            [2,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,3],
            [0,0,0,0,0,0,0,0],
            [1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1]
        ],
        [
            [2,0,0,0,0,0,1,1],
            [0,0,0,0,0,0,1,1],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [1,1,0,0,0,0,0,0],
            [1,1,0,0,0,0,0,3]
        ],
        [
            [0,0,0,0,0,0,0,0],
            [0,0,0,1,1,1,1,1],
            [1,1,1,0,0,0,0,0],
            [1,0,0,0,0,0,0,3],
            [1,0,0,0,0,0,0,0],
            [1,0,0,0,0,1,1,1],
            [1,0,0,0,0,1,1,1],
            [1,0,0,2,0,1,1,1]
        ],
        [
            [1,1,0,0,0,0,0,3],
            [1,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,1],
            [2,0,0,0,0,0,1,1]
        ],
        [
            [1,1,0,0,3,0,1,1],
            [1,1,0,0,0,0,1,1],
            [1,1,0,0,0,0,1,1],
            [1,1,0,0,0,0,1,1],
            [1,1,0,0,0,0,1,1],
            [1,1,0,0,0,0,1,1],
            [1,1,0,0,0,0,1,1],
            [1,1,0,2,0,0,1,1]
        ]
    ],
    "Hard":[
        [
            [2,0,1,0,0,0,0,0],
            [0,0,1,0,0,1,0,0],
            [0,0,1,0,0,1,1,0],
            [0,0,1,0,0,1,0,0],
            [0,0,1,0,0,1,0,0],
            [0,0,1,0,0,1,0,1],
            [0,0,1,0,0,1,0,0],
            [0,0,0,0,0,1,0,3]
        ],
        [
            [1,0,0,0,0,0,1,1],
            [1,0,0,1,0,0,0,0],
            [1,0,1,1,1,1,0,0],
            [1,0,1,2,0,1,0,0],
            [1,0,0,1,0,1,1,0],
            [3,1,0,0,0,1,0,0],
            [0,1,1,1,1,1,0,1],
            [0,0,0,0,0,0,0,1]
        ],
        [
            [0,0,0,0,0,0,1,1],
            [0,1,0,1,1,0,0,0],
            [0,0,1,1,1,1,0,0],
            [0,0,0,1,0,0,0,0],
            [0,0,0,0,1,0,0,0],
            [0,0,1,1,1,1,0,0],
            [0,0,0,1,1,0,1,3],
            [1,2,0,1,1,0,0,1]
        ],
        [
            [0,1,3,0,0,0,0,0],
            [0,1,1,1,1,1,1,0],
            [0,1,0,1,0,1,0,0],
            [0,0,0,1,0,1,0,1],
            [0,1,0,1,0,1,0,0],
            [0,1,0,1,0,1,1,0],
            [0,1,0,1,0,0,0,0],
            [2,1,0,0,0,1,0,0]
        ]
    ]
}



class lockdown:

    def __init__(self,ownerIP,senseHATobj:senseHAT,hasBomb = False):
        self.maze:list[list[int]] = []
        self.playerPosition = {
            "x":0,
            "y":0
        }
        self.playerspawn = [0,0]
        self.exit = [0,0]
        self.hasBomb = hasBomb
        self.ownerIP = ownerIP
        self.senseHAT = senseHATobj
        self.timeToComplete = 60

    def getMaze(self,Hard:bool):
        if Hard:
            self.maze.append(mazes["Hard"][randint(0,len(mazes["Hard"])-1)])
        else:
            self.maze.append(mazes["Normal"][randint(0,len(mazes["Normal"])-1)])
        

        for i in range(len(self.maze[0])):
            for ii in range(len(self.maze[0][i])):
                if self.maze[0][i][ii] == 2:
                    self.playerspawn = [ii,i]
                elif self.maze[0][i][ii] == 3:
                    self.exit = [ii,i]
        self.playerPosition["x"] = self.playerspawn[0]
        self.playerPosition["y"] = self.playerspawn[1]
        print(self.playerspawn)
        print(self.exit)
            


    def mode_test(self):
        finished = False
        while not finished:
            available = True
            sleep(0.2)
            if keyboard.is_pressed("left") and available:
                self.playerPosition["x"] += -1
            elif keyboard.is_pressed("right") and available:
                self.playerPosition["x"] += 1
            elif keyboard.is_pressed("up") and available:
                self.playerPosition["y"] += -1
            elif keyboard.is_pressed("down") and available:
                self.playerPosition["y"] += 1
            
            available = False

            finished = self.checkPlayerPosition()
            self.displayMaze()
        self.senseHAT.clearSenseLED(0,255,0)

    def mode_prod(self):
        finished = False
        failed = False
        now = datetime.now()
        seconds_since_midnight = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
        finalTime = seconds_since_midnight + self.timeToComplete
        while not finished:
            available = True
            now2 = datetime.now()
            sleep(0.2)
            if keyboard.is_pressed("left") and available:
                self.playerPosition["x"] += -1
            elif keyboard.is_pressed("right") and available:
                self.playerPosition["x"] += 1
            elif keyboard.is_pressed("up") and available:
                self.playerPosition["y"] += -1
            elif keyboard.is_pressed("down") and available:
                self.playerPosition["y"] += 1
            
            available = False
            if (now2 - now2.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds() == finalTime:
                finished = True
                failed = True
            else:
                finished = self.checkPlayerPosition()
            self.translateMaze2DArrayToSenseReadable()

            
        if failed:
            self.senseHAT.clearSenseLED(0,0,0)
        else:
            self.senseHAT.clearSenseLED(0,255,0)
            self.ifHasBomb()
        


    def ifHasBomb(self):
        if self.hasBomb:
            self.senseHAT.displayMessage("Catalyst Defused",0,255,0)
            get(url=f"{self.ownerIP}:8000/lockdown/complete") # I forgot which port flask hosts with
        else:
            self.senseHAT.displayMessage("The Catalyst isn't here",255,0,0)


    def checkPlayerPosition(self):
        if 0 > self.playerPosition["y"]:
            self.playerPosition["y"] += 1
        elif self.playerPosition["y"] == len(self.maze[0]):
            self.playerPosition["y"] += -1

        elif self.playerPosition["x"] == len(self.maze[0][0]):
            self.playerPosition["x"] += -1
        elif 0 > self.playerPosition["x"]:
            self.playerPosition["x"] += 1
        # fantastic ahh code
        if [self.playerPosition["x"],self.playerPosition["y"]] == self.exit:
            return True
        if self.maze[0][self.playerPosition["y"]][self.playerPosition['x']] == 1:
            self.senseHAT.clearSenseLED(255,0,0)
            sleep(1)
            self.playerPosition["x"] = self.playerspawn[0]
            self.playerPosition["y"] = self.playerspawn[1]
        return False

    def displayMaze(self):
        print("\n"*60)
        copymaze = copy.deepcopy(self.maze)
        copymaze[0][self.playerPosition["y"]][self.playerPosition["x"]] = "#"
        for i in copymaze[0]:
            print(i)
            # print(self.playerPosition["x"])
            # print(self.playerPosition["y"])
    

    def translateMaze2DArrayToSenseReadable(self):
        copymaze = copy.deepcopy(self.maze)
        copymaze[0][self.playerPosition["y"]][self.playerPosition["x"]] = "#"
        final = []
        for i in copymaze[0]:
            for ii in i:
                final.append(colordict[ii])
        self.senseHAT.set_pixel(final)
        
            

        

if __name__ == "__main__":
    x = lockdown()
    x.getMaze(True)
    x.mode_test()



'''
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0]
'''