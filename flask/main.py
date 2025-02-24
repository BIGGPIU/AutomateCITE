from flask import Flask, render_template, request
import webbrowser
import os 
# from datetime import datetime
# from datetime import time
import time
from senseHAT import senseHAT
from picam import Camera
import requests
# I think this dict should be used as an IP:dict{component:function} kind of thing
# or maybe something else I just have to think of it. uhhh idk 
pi:dict[dict] = {
    "172.20.72.68": {
        "senseHAT":senseHAT("127.0.0.1")
    },
    "127.0.0.1": {
        "camera":Camera("127.0.0.1")
    }
} 

objects = {
        "restart_signal":0 # if this is 1 then you should restart
    }

app = Flask(__name__)
@app.route("/")
def main():
    forcereset = True
    if request.method == "GET":
        for i in request.args.keys():
            print(i)
            if "senseHATtxt" in i:
                if request.args.get(i) != None:
                    # print(request.args.get(i).split(","))
                    y = i.split(",")[1]
                    temp = request.args.get(i).replace(" ","_")
                    # print(f"http://{y}:8000/sensehat/sendmessage/{temp}")
                    # requests.post(f"http://{y}:8000/sensehat/sendmessage/{temp}")
            if i[0] == "r" and i[1] == ",":
                r = request.args.get(i)
                g = request.args.get("g")
                b = request.args.get("b")
                y = i.split(",")[1]
                print (f"http://{y}:8000/sensehat/clear/{r}/{g}/{b}")
                # requests.post(f"http://{y}:8000/sensehat/clear/{r}/{g}/{b}")
            if "showconstantcstm" in i:
                y = i.split(",")[1]
                temp = request.args.get(i)
                print(f"http://{y}:8000/sensehat/sendmessage/{temp}/permanent)")
                # requests.post(f"http://{y}:8000/sensehat/sendmessage/{temp}")
            if "showconstant" in i:
                y = i.split(",")[1]
                if request.args.get(i) == "time":
                    requests.post(f"http://{y}:8000/sensehat/display/time")
                if request.args.get(i) == "coundown":
                    requests.post(f"http://{y}:8000/sensehat/display/countdown")
  
        objects["restart_signal"] = 0
        if len(request.args) != 0 and forcereset:
            objects["restart_signal"] = 1

        
        
        
        return render_template("main2.html",dictionary=pi,restartsignal=objects["restart_signal"])
        


        
        


if __name__ == "__main__":
    # app.run()
    # webbrowser.open("127.0.0.1:5000",new=2)
    os.system("flask --app main run --host=0.0.0.0")
    # actually I forgot how to run a flask server  publically