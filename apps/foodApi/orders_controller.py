from flask import request, jsonify
from flask_socketio import send, emit
from apps.foodApi.validators import validate_schema
from app import socketio


@validate_schema("order_request")
def create():
    socketio.emit("order_received", {'data': request.get_json() })
    return jsonify({"message": "La orden ha sido recibida correctamente "}), 200
