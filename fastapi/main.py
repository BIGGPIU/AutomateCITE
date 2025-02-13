from fastapi import FastAPI
from senseHAT import senseHAT
from fastapi.responses import FileResponse
from picam import Camera
from datetime import datetime as dt
from time import sleep
import asyncio
from concurrent.futures import ThreadPoolExecutor

app = FastAPI(
    title="Local RPi API",
    version="1.0.0"
)

display_Eternal = True
@app.get("/ping")
async def ping():
    global display_Eternal
    print("ping!")
    display_Eternal = False
    return "pong"
@app.post("/sensehat/sendmessage/{message}")
async def display_message(message):
    global display_Eternal # bad code practice my ass 
    display_Eternal = False
    message.replace("_"," ")
    x = senseHAT()
    x.displayMessage(message)
@app.post("/sensehat/clear/{r}/{g}/{b}")
async def clearLEDs(r,g,b):
    global display_Eternal  
    display_Eternal = False
    x = senseHAT()
    x.clearSenseLED(r,g,b) 
@app.get("/camera/snap")
async def snap():
    global display_Eternal 
    x = Camera()

    return FileResponse(x.snap())
@app.get("/sensehat/display/time")
async def showTime(): #if you call this showtime not show time then youre stupid
    # x = senseHAT()
    global display_Eternal 
    display_Eternal = True
    
    while display_Eternal:
        await displayTime()

async def displayTime():
    await asyncio.sleep(1)
    y = dt.now()
    print(display_Eternal)
    # sleep(1)
    print(y.strftime("%H:%M %p"))
    # return 1
    # x.displayMessage(y.strftime("%H:%M %I"))

