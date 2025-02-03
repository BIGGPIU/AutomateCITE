from sense_hat import SenseHat

sense = SenseHat()

class senseHAT:
    
    def __init__(self,ip):
        self.ip = ip


    def displayMessage(message:str,r:int,g:int,b:int):
        sense.show_message(message,text_colour=(r,g,b))

    def clear(r:int,g:int,b:int):
        sense.clear((r,g,b))

    def generateHTML():
        return 