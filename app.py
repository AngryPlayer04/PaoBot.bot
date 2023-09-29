from flask import Flask, render_template
import json
import requests
import threading
from functools import partial


event = threading.Event()
#user_id = '319963626108878848'

with open("config.json", "r") as config:
    data = json.load(config)
    token = data["token"]

app = Flask(__name__)

reqUrl = "https://discord.com/api/v10/users/319963626108878848"

def avatar():  # sourcery skip: hoist-statement-from-loop, inline-immediately-returned-variable, inline-variable, remove-unreachable-code
    

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
        event.wait(60)


@app.route('/')
def index():
    return render_template('index.html',  avatar=f'https://cdn.discordapp.com/avatars/319963626108878848/{avatar()}.png')

if __name__ == '__main__':

    #app.run(debug=True)
    
    serve(app, host="0.0.0.0", port=8080)

    