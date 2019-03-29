import os
from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy

#configuraciones de la applicacion
template_path = "apps/foodWeb/templates/"
app = Flask(__name__, template_folder=template_path)
app.config['SECRET_KEY'] = 'secret!'

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "bookdatabase.db"))
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)

app.config.from_pyfile('config.py')
socketio = SocketIO(app)