from flask import Flask, render_template
import json
import requests
import threading
from threading import Thread
from functools import partial
from waitress import serve


event = threading.Event()
#user_id = '319963626108878848'

with open("config.json", "r") as config:
    data = json.load(config)
    token = data["token"]

app = Flask(__name__)

reqUrl = "https://discord.com/api/v10/users/319963626108878848"



def avatar():  
    

    while True:
        headersList = {
            "Accept": "*/*",
            "Authorization": f"Bot {token}" 
        }
        payload = ""
        reqUrl = "https://discord.com/api/v10/users/319963626108878848"

        payload = ""

        response = requests.request("GET", reqUrl, data=payload,  headers=headersList).json()
        hashav = response['avatar']
        return hashav
        event.wait(250)


@app.route('/')
def index():
    return render_template('index.html',  avatar=f'https://cdn.discordapp.com/avatars/319963626108878848/{avatar()}.png')

partial_run = partial(app.run, host="0.0.0.0", port=8080, debug=True, use_reloader=False)

if __name__ == '__main__':
    t = Thread(target = partial_run)
    t.start()
    avatar()
    #app.run(debug=True)
    
    #serve(app, host="0.0.0.0", port=8080)

    
