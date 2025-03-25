from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from time import sleep
from selenium.webdriver.remote.webelement import WebElement
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
        charactersHours = ["a","b","c"]
        charactersMinutes = ["d","e","f","g","h","i","j","k"]
        final = ""
        for i in range(len(binary["hours"])):
            if binary["hours"][i] == 1:
                final += charactersHours[i]
        for i in range(len(binary["minutes"])):
            if binary["minutes"][i] == 1:
                final += charactersMinutes[i]
        return final
            

class Printers:

    __slots__ = ("driver","printerLandingPageLink","printers","currentPrinter","webTimeout","time")

    def __init__(self,driver):
        self.driver:webdriver.Firefox = driver 
        self.printerLandingPageLink:str = "http://172.20.71.116/"
        self.printers:WebElement = []
        self.currentPrinter:int = 0
        self.webTimeout:int = 2
        self.time:int = 0


    def getPrinters(self,goToLanding = False) -> None:
        try:
            if goToLanding:
                self.driver.get(self.printerLandingPageLink)
        except:
            print("cannot access print page")
        
        sleep(self.webTimeout)

        x = self.driver.find_elements(By.CLASS_NAME,"nav-arrow")
        x[0].click()
        del x 

        self.printers = self.driver.find_elements(By.CSS_SELECTOR,"[role=menuitem]")
        
    def incrementPrinter(self) -> None:
        # goes to the next printer and returns the time left
        self.currentPrinter += 1
        if self.currentPrinter == len(self.printers):
            self.currentPrinter = 0

        # x = self.driver.find_elements(By.CLASS_NAME,"nav-arrow")
        # x[0].click()

        try:
            self.printers[self.currentPrinter].click()
        except:
            pass

        sleep(self.webTimeout)
        try:
            time = self.driver.find_element(By.CSS_SELECTOR,"div.mb-0 > div:nth-child(1) > div:nth-child(1) > span:nth-child(3)")
            self.time = self.processTime(time.text)
            sleep(self.webTimeout)
            self.getPrinters()
        except:
            self.time = 0

    def getPrinterTime(self) -> None:
        try:
            time = self.driver.find_element(By.CSS_SELECTOR,"div.mb-0 > div:nth-child(1) > div:nth-child(1) > span:nth-child(3)")
            if ":" in time:
                self.time = self.processTime(time.text)
            else:
                self.time = 0
        except:
            self.time = 0

    def calculateTime(self):
        timecopy = self.time
        binary = {
            "hours":[0,0,0],
            "minutes":[0,0,0,0,0,0]
        }
        hours = 0
        minutes = 0
        while timecopy > 60:
            timecopy += -60
            hours += 1
        minutes += timecopy

        if hours != 0 and hours % 2 == 1:
            binary["hours"][0] = 1
            hours += -1

        for i in range(len(binary["hours"])):
            ival = abs(i - len(binary["hours"]))
            if i == 0:
                continue
            if hours - (2**ival) >= 0:
                hours -= (2**ival)
                binary["hours"][ival] = 1
        

        if minutes != 0 and minutes % 2 == 1:
            binary["minutes"][0] = 1
            minutes += -1
        for i in range(len(binary["minutes"])):
            ival = abs(i - len(binary["minutes"]))
            if i == 0 and minutes != 0:
                continue
            if minutes == 0:
                return binary
            if (minutes - (2**ival) ) >= 0:
                binary["minutes"][ival] = 1
                minutes += -(2**ival)
        return binary


    def calculateTime2(time):
        # timeStr = str(time)
        timecopy = time
        binary = {
            "hours":[0,0,0],
            "minutes":[0,0,0,0,0,0]
        }
        hours = 0
        minutes = 0
        while timecopy > 60:
            timecopy += -60
            hours += 1
        minutes += timecopy

        if hours != 0 and hours % 2 == 1:
            binary["hours"][0] = 1
            hours += -1

        for i in range(len(binary["hours"])):
            ival = abs(i - len(binary["hours"]))
            if i == 0:
                continue
            if hours - (2**ival) >= 0:
                hours -= (2**ival)
                binary["hours"][ival] = 1
        

        if minutes != 0 and minutes % 2 == 1:
            binary["minutes"][0] = 1
            minutes += -1
        for i in range(len(binary["minutes"])):
            ival = abs(i - len(binary["minutes"]))
            if i == 0 and minutes != 0:
                continue
            if minutes == 0:
                return binary
            if (minutes - (2**ival) ) >= 0:
                binary["minutes"][ival] = 1
                minutes += -(2**ival)
        # if int(timeStr[-1]) in [1,3,5,7,9]:
        #     binary[0] = 1
        #     timecopy += -1
        
        # for i in range(len(binary)):
        #     ival = abs(i - len(binary))
        #     if i == 0:
        #         continue
        #     else:
        #         if timecopy == 0:
        #             return binary
        #         if timecopy - (2**ival) >= 0:
        #             binary[ival] = 1
        #             timecopy += -(2**ival)
        # return binary

        return binary


    def processTime(self,time:str) -> int:
        finalTime = 0
        time:list[str] = time.split(":")
        time.pop()
        for i in range(len(time)):
            time[i] = int(time[i])
            if i == 0:
                finalTime += 60*time[i]
            if i == 1:
                finalTime += time[i]
        return finalTime
    

    def getDriver():
        return webdriver.Firefox(options=Options())

        
# div.mb-0 > div:nth-child(1) > div:nth-child(1) > span:nth-child(3)



if __name__ == "__main__":
    
    # driver = webdriver.Firefox(options=Options())
    # x = Printers(driver)
    # x.getPrinters()
    # x.incrementPrinter()
    # #x.incrementPrinter()
    # x.calculateTime()

    # Serials.findArduino()

    while True:
        sleep(1)
        x = random.randint(1,400)
        y = (Printers.calculateTime2(x))
        ans = 0
        for i in range(len(y["hours"])):
            if y["hours"][i] == 1:
                if i == 0:
                    ans+=60
                else:
                    ans+=(2**i)*60
        

        for i in range(len(y["minutes"])):
            if (y["minutes"][i]) == 1:
                if i == 0:
                    ans+=1
                else:
                    ans+=(2**i)
        
        print (ans)
        print (x)

    #     for i in range(len(y)):
    #         if y[0] == 1 and i == 0:
    #             ans +=1
    #             continue
    #         if y[i] == 1:
    #             ans += 2**i
    #     print(ans)
    #     print (y)


    
    



