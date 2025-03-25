from fastapi import FastAPI
from readSerial import *
from yandev import *

app = FastAPI(
    title="Print API",
    version="1.0.0"
)


@app.get("/")
async def getTime():
    ser = serial.Serial(port=Serials.findArduino())
    return Binary.binaryTointeger(readDuration(ser=ser))

@app.get("/increment")
async def incrementPrinter():
    #use this to send the current printer 
    pass