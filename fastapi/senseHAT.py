from sense_hat import SenseHat
from datetime import datetime,timedelta



class senseHAT:
    
    def __init__(self):
        self.sense = SenseHat()
        self.sense.set_rotation(180)

    def set_pixel(self,array):
        self.sense.set_pixels(array)

    def displayMessage(self,message:str,r:int=255,g:int=255,b:int=255):
        self.sense.show_message(message,text_colour=[r,g,b])

    def hex_to_rgb(hex):
        return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
    
    def clearSenseLED(self,r,g,b):
        self.sense.clear((r,g,b))

    def getTimeUntilNextClass(self) -> str:
        currentTime = datetime.now()
        hours = currentTime.hour
        minutes = currentTime.minute
        timeUntilNextClass:int 
        if (hours == 8 and minutes >= 15) or ( hours == 9 and minutes <= 45):
            timeUntilNextClass = str(timedelta(hours=9,minutes=45) - timedelta(hours=hours,minutes=minutes))
            timeUntilNextClass = timeUntilNextClass.split(":")
            timeUntilNextClass.pop()
            timeUntilNextClass = 'Time until Next class: ' + ":".join(timeUntilNextClass)
        elif (hours == 9 and minutes >= 50) or (hours == 10) or (hours == 11 and minutes <= 12):
            timeUntilNextClass = str(timedelta(hours=11,minutes=12) - timedelta(hours=hours,minutes=minutes))
            timeUntilNextClass = timeUntilNextClass.split(":")
            timeUntilNextClass.pop()
            timeUntilNextClass = 'Time until Next class: ' + ":".join(timeUntilNextClass)
        elif (hours == 11 and minutes >= 20) or (hours == 12) or (hours == 13 and minutes <= 15):
            timeUntilNextClass = str(timedelta(hours=13,minutes=15) - timedelta(hours=hours,minutes=minutes))
            timeUntilNextClass = timeUntilNextClass.split(":")
            timeUntilNextClass.pop()
            timeUntilNextClass = 'Time until Next class: ' + ":".join(timeUntilNextClass)
        elif (hours == 13 and minutes >= 23) or (hours == 14):
            timeUntilNextClass = str(timedelta(hours=14,minutes=45) - timedelta(hours=hours,minutes=minutes))
            timeUntilNextClass = timeUntilNextClass.split(":")
            timeUntilNextClass.pop()
            timeUntilNextClass = 'Time until Next class:  ' + ":".join(timeUntilNextClass)
            
        elif (hours > 14):
            timeUntilNextClass = "No classes upcoming"
        else:
            timeUntilNextClass = "Transitioning to next class"

        if len(timeUntilNextClass) == 0:
            timeUntilNextClass = "ERR"
        return timeUntilNextClass
    # def generateHTML():
    #     return 
    