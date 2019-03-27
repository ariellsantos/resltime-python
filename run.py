from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config.from_pyfile('config.py')
socketio = SocketIO(app)

if __name__ == '__main__':
    socketio.run(app)