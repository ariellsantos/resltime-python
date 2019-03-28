from flask import request
from flask_socketio import send, emit
from apps.foodApi.validators import validate_schema
from app import socketio


@validate_schema("order_request")
def create():
    socketio.emit("order_received", {'data': 42 })
    return "ok"
