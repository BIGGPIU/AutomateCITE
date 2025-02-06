from fastapi import FastAPI
from senseHAT import senseHAT
from fastapi.responses import FileResponse
from picam import Camera
app = FastAPI(
    title="Local RPi API",
    version="1.0.0"
)



@app.post("/sensehat/sendmessage/{message}")
async def display_message(message):
    message.replace("_"," ")
    x = senseHAT()
    x.displayMessage(message)
@app.post("/sensehat/clear/{r}/{g}/{b}")
async def clearLEDs(r,g,b):
    x = senseHAT()
    x.clearSenseLED(r,g,b) 
@app.get("/camera/snap")
async def snap():
    x = Camera()

    return FileResponse(x.snap())