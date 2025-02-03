from flask import Flask, render_template, request
import webbrowser
import os 
from senseHAT import senseHAT
import requests
# I think this dict should be used as an IP:dict{component:function} kind of thing
# or maybe something else I just have to think of it. uhhh idk 
pi:dict[dict] = {
    "172.20.72.68": {
        "senseHAT":senseHAT("127.0.0.1")
    }
} 

app = Flask(__name__)
@app.route("/")
def main():
    objects = {
        "restart_signal":0 # if this is 1 then you should restart
    }
    if request.method == "GET":
        # print(request.args)
        for i in request.args.keys():
            # print(i)
            if "senseHATtxt" in i:
                if request.args.get(i) != None:
                    # print(request.args.get(i).split(","))
                    y = i.split(",")[1]
                    temp = request.args.get(i).replace(" ","_")
                    # print(f"http://{y}:8000/sensehat/sendmessage/{temp}")
                    # requests.post(f"http://{y}:8000/sensehat/sendmessage/{temp}")
        if len(request.args) != 0:
            objects["restart_signal"] = 1
       
        
        html = []

        for i in pi.keys():
            html.append(f"""
 <div class="pi">
                <div class="pipee">Raspberry pi at {i}</div>""")
        return render_template("main.html",dictionary=pi,restartsignal=objects["restart_signal"])
        


        
        


if __name__ == "__main__":
    app.run()
    # webbrowser.open("127.0.0.1:5000",new=2)
    os.system("flask run --host=0.0.0.0")
    # actually I forgot how to run a flask server  publically