from fastapi import FastAPI
from senseHAT import senseHAT

app = FastAPI(
    title="Local RPi API",
    version="1.0.0"
)



@app.get("/sensehat/sendmessage/{message}")
async def display_message(message):
    x = senseHAT()
    x.displayMessage(message)
        