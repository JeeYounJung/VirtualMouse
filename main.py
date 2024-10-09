from flask import Flask, request, jsonify, Response
import os
import subprocess
from pynput.keyboard import Controller, Key, Listener

app = Flask(__name__)
virtual_mouse_process = None

@app.route('/')
def home():
    with open("web.html") as f:
        html = f.read()

    return html

def start():
    global virtual_mouse_process
    try:
        # result = subprocess.run(["python", "virtualMouse.py"])
        # return result.stdout
        virtual_mouse_process = subprocess.Popen(["python", "virtualMouse.py"])
        
    except Exception as e:
        return str(e)


@app.route('/start')
def start_route():
    return start()

def end():
    global virtual_mouse_process
    if virtual_mouse_process:
        try:
            virtual_mouse_process.terminate()
            # return terminate
        except Exception as e:
            str(e)
    else:
        return
    


# /start 라우트에 start 함수 연결
@app.route('/end')
def end_route():
    return end()

if __name__=="__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'), 
            port=int(os.getenv('PORT', 4444)))

