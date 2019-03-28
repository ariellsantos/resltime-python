from functools import wraps
import json
from cerberus import Validator
from flask import current_app
from utils.tools import Tools
from .schemas_rules import schemas
from flask import request, jsonify




def validate_schema(schema_name):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kw):
            try:
                schema_rules = (schemas.get(schema_name))
                data_request = request.get_json()
                response = validate(schema_rules, data_request)
                if response != None:
                    return response
            except:
                return jsonify({"error": "An unknow error has ocurred"}), 500
            return f(*args, **kw)
        return wrapper
    return decorator

def validate(schema_rules, data_request):
    validator_json = Validator(schema_rules)
    result_validator = validator_json.validate(data_request)
    if(result_validator != True):
        return jsonify({"error": validator_json.errors}), 400




class Validator(Validator):
    pass
