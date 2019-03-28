from app import app, socketio
from apps.foodApi.urls import api_urls
from apps.foodWeb.urls import web_urls

app.register_blueprint(api_urls)
app.register_blueprint(web_urls)


if __name__ == '__main__':
    socketio.run(app, debug=True)
