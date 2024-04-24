from flask import Flask
from flask_cors import CORS

from main.routes.logs_routes import event_route_blueprint
from models.settings.connection import db_connection_handler
from main.service.service_redis import redis_service

db_connection_handler.connect_to_db()

redis_service.run()

app = Flask(__name__)

CORS(app)

app.register_blueprint(event_route_blueprint)
