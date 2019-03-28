from flask import Blueprint

from .controller import index

web_urls = Blueprint('web_urls', __name__, url_prefix='/admin')

web_urls.add_url_rule('/orders/', 'index', view_func=index, methods=['GET'])
