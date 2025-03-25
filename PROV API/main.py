import serial.tools
import serial.tools.list_ports
from yandev import *
import pyautogui
import serial

# TODO
# REMAKE THE CALCULATETIME FUNCTION TO OUTPUT TIME AS [H,H,H,M,M,M,M,M,M,M] OR AS A DICTIONARY ACTUALLY MAKE IT A DICTIONARY

if __name__ == "__main__":
    driver = Printers.getDriver()
    # y = Serials.findArduino()
    ser = serial.Serial(port=Serials.findArduino())

    printer = Printers(driver)
    printer.getPrinters(goToLanding=True)
    printer.incrementPrinter()
    printer.getPrinterTime()
    x = printer.calculateTime()
    x = Serials.convertBinaryToText(x)
    ser.write(str.encode(x))
    while True:
        sleep(5)
        printer.getPrinterTime()
        if (x != Serials.convertBinaryToText(printer.calculateTime())):
            ser.write(str.encode(x))
            x = Serials.convertBinaryToText(printer.calculateTime())
            ser.write(str.encode(x))
        if printer.time == 0:
            printer.incrementPrinter()
        # ser.write(x)

        
        