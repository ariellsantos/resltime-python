import pytest
from apps.foodApi.validators  import validate


def test_validate():
    '''
    Valida que el request cumple con las reglas descritas por el esquema
    '''
    schema_request = {
        'name': "ariel"
    }
    schema_rules = {
        'name':{
            'type': "string",
            'min': 2,
            'max': 10,
            'required': True
        }
    }
    result = validate(schema_rules, schema_request)
    assert  result == None