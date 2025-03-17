import serial


def readDuration():
    s = serial.Serial()
    return s.read(4)