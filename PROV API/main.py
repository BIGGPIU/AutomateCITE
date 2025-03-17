from yandev import *
import pyautogui
import serial



if __name__ == "__main__":
    driver = Printers.getDriver()

    ser = serial.Serial(port=Serials.findArduino())

    printer = Printers(driver)
    printer.getPrinters()
    printer.incrementPrinter()
    while True:
        sleep(5)
        printer.getPrinterTime()
        x = printer.calculateTime()
        x = Serials.convertBinaryToText(x)
        ser.write(x)

        
        