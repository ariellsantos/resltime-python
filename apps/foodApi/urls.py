from flask import Blueprint

from .controller import create

api_urls = Blueprint('api_urls', __name__, url_prefix='/api')

api_urls.add_url_rule('/orders/', 'create', view_func=create, methods=['POST'])
