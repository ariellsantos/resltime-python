schemas = {
    'order_request':   {
        'telefono_cliente':{
            'type': "string",
            'min': 7,
            'max': 10,
            'required': True
        },
        'direccion_cliente': {
            'type': "string",
            'min': 3,
            'required': True
        },
        'orden': {
            'type': "string",
            'min': 5,
            'required': True
        },
        'nombre_cliente': {
            'type': "string",
            'min':3,
            'required': True
        }
    }
}