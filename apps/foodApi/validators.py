from functools import wraps
import json
from cerberus import Validator
from flask import current_app
from .schemas_rules import schemas
from flask import request, jsonify




def validate_schema(schema_name):
    '''
    Decorador para validar que la estructura y datos del body sean correctos
    **parametros**, **return**
     :param schema_name:  nombre del esquema a evaluar
     :type schema_name: string
     :return: el esquema es invalido retorna un status http 400
    '''
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
    '''
    Compara el esquema recibido  en el request con las reglas para validar el esquema
    **parametros**
    :param schema_rules: son las reglas en las que el esquema debe ser valido
    :param data_request:esquema json resivido en la petición
    :type schema_rules: dict
    :type data_request: dict
    :return: retorna una respuesta con codigo http 400 en caso de no ser valido
    '''
    validator_json = Validator(schema_rules)
    result_validator = validator_json.validate(data_request)
    if(result_validator != True):
        return jsonify({"error": validator_json.errors}), 400




class Validator(Validator):
    '''
    Clase construida en base al validador de esquemas proveeido por el modulo cerberus
    '''
    pass
