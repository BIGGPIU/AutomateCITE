#from sense_hat import SenseHat



class senseHAT:
    
    def __init__(self):
        self.sense = SenseHat()


    def displayMessage(self,message:str,r:int=255,g:int=255,b:int=255):
        self.sense.show_message(message,text_colour=(r,g,b))

    def hex_to_rgb(hex):
        return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
    
    def clearSenseLED(self,r,g,b):
        self.sense.clear((r,g,b))

    # def generateHTML():
    #     return 
    