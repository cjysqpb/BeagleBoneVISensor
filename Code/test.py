#!/usr/bin/env python
from gevent import monkey
import time
from threading import Thread
from flask_socketio import SocketIO
from FlaskWebProject1 import app
thread = None
socketio = SocketIO(app)

def background_thread():
    count = 0
    
    while True:
        time.sleep(5)
        print("Hello World")
        count += 1
        print(count)
        
if __name__ == '__main__':
    if thread is None:
        thread = Thread(target=background_thread)
        #thread.daemon = True
        thread.start()
    socketio.run(app,'0.0.0.0',8000)