# registro del urls para el API
from flask import Blueprint

from .orders_controller import create
#Registro de urls
api_urls = Blueprint('api_urls', __name__, url_prefix='/api')

api_urls.add_url_rule('/orders/', 'create', view_func=create, methods=['POST'])
