from flask import Flask, render_template
from flask_socketio import SocketIO

template_path = "apps/foodWeb/templates/"
app = Flask(__name__, template_folder=template_path)
app.config['SECRET_KEY'] = 'secret!'


app.config.from_pyfile('config.py')
socketio = SocketIO(app)