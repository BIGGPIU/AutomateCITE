from time import sleep
import random
import serial
import serial.tools
import serial.tools.list_ports
class Serials:
    
    def findArduino() -> str:
        sercom = serial.tools.list_ports.comports()
        for i in sercom:
            if "Arduino Uno" in i.description:
                return i.device        
        return "no arduino found"
    
    def convertBinaryToText(binary:list[int]) -> str:
        characters = ["a","b","c","d","e","f","g","h","i","j","k"]
        final = ""
        for i in range(len(binary)):
            if binary[i] == 1:
                final += characters[i]
        return final
    

class Binary:

    def binaryTointeger(binary:str) -> dict[str:int]:
        # im not gonna insult your intelligence by adding 
        # what type this is gonna return 
        hours = 0
        minutes = 0
        for i in range(len(binary)):
            valToadd = 0
            if 2 >= i:
                if i == 0:
                    valToadd=1
                else:
                    valToadd = 2**i
                if binary[i] != "~":
                    hours += valToadd
            else:
                if i-3 == 0:
                    valToadd = 1
                else:
                    valToadd = 2**(i-3)
                if binary[i] != "~":
                    minutes += valToadd
        return {"hours":hours,"minutes":minutes}