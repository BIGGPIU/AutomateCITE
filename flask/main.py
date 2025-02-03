from flask import Flask, render_template, request
import webbrowser
import os 
from senseHAT import senseHAT
# I think this dict should be used as an IP:dict{component:function} kind of thing
# or maybe something else I just have to think of it. uhhh idk 
pi:dict[dict] = {
    "127.0.0.1": {
        "senseHAT":senseHAT("127.0.0.1")
    }
} 

app = Flask(__name__)
@app.route("")
def main():
    objects = {
        "restart_signal":0 # if this is 1 then you should restart
    }
    if request.method == "GET":
        if len(request.args.get()) != 0:
            objects["restart_signal"] = 1
        
        html = []

        for i in pi.keys():
            for ii in i.keys():
                html.append(pi[i][ii].generateHTML())
        


        
        


if __name__ == "__main__":
    app.run()
    webbrowser.open("127.0.0.1:5000",new=2)
    os.system("flask run --host=0.0.0.0")
    # actually I forgot how to run a flask server  publically