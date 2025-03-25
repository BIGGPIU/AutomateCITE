import serial
from time import sleep
from yandev import *



def readDuration(ser:serial.Serial):
    x = ser.read(9)
    y = bytes.decode(x)
    # print (x)
    # print (y)
    return y


if __name__ == "__main__":
    ser = serial.Serial(port=Serials.findArduino())

    while True:
        print(Binary.binaryTointeger(readDuration(ser)))