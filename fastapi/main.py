from fastapi import FastAPI
from senseHAT import senseHAT
# from sense_hat import SenseHat
from fastapi.responses import FileResponse
from picam import Camera
from datetime import datetime as dt
from time import sleep
import asyncio
from concurrent.futures import ThreadPoolExecutor
import socket
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.254.254.254', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


x = senseHAT()
for i in range(10):
    x.displayMessage(get_ip())
    sleep(2)

del x
    

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
    message = message.replace("_"," ")
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
    x = senseHAT()
    global display_Eternal 
    display_Eternal = True
    
    while display_Eternal:
        await displayTime(x)

async def displayTime(x:senseHAT):
    await asyncio.sleep(1)
    y = dt.now()
    print(display_Eternal)
    # sleep(1)
    # print(y.strftime("%H:%M %p"))
    # return 1
    x.displayMessage(y.strftime("%H:%M %I")) # I know this isnt right I'll fix it soontm


@app.post("/sensehat/sendmessage/{message}/permanent")
async def showCustomMessage(message):
    global display_Eternal
    
    if display_Eternal:
        display_Eternal = False

    display_Eternal = True
    message = message.replace("_"," ")
    x = senseHAT()
    while display_Eternal:
        x.displayMessage(message)
        await asyncio.sleep(1)


@app.get("/sensehat/display/countdown")
async def countdown():
    global display_Eternal

    if display_Eternal:
        display_Eternal = False
    
    display_Eternal = True

    x = senseHAT()
    while display_Eternal:
        x.displayMessage(x.getTimeUntilNextClass())
        await asyncio.sleep(3)