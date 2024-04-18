from flask import Blueprint, request, jsonify
from http_types.http_request import HttpRequest
from data.logs_handler import LogsHandler
from errors.error_handler import handle_error
from http_types.http_response import HttpResponse
from models.constants.tags_enum import tags_enum

event_route_blueprint = Blueprint("log_route", __name__)


@event_route_blueprint.route("/logs", methods=["POST"])
def add_log():
    try:
        http_request = HttpRequest(body=request.json, param=request.args.to_dict()) 
        logs_handler = LogsHandler()

        http_response = logs_handler.add_log(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_error(exception)
        return jsonify(http_response.body), http_response.status_code


@event_route_blueprint.route("/logs/<log_id>", methods=["GET"])
def get_log_by_id(log_id):
    try:
        http_request = HttpRequest(param={"log_id": log_id})
        logs_handler = LogsHandler()

        http_response = logs_handler.get_log_by_id(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_error(exception)
        return jsonify(http_response.body), http_response.status_code


@event_route_blueprint.route("/logs/tag/<tag>/count", methods=["GET"])
def count_logs_by_tag(tag):
    try:
        http_request = HttpRequest(param={"tag": tag})
        logs_handler = LogsHandler()

        http_response = logs_handler.count_logs_by_tag(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_error(exception)
        return jsonify(http_response.body), http_response.status_code


@event_route_blueprint.route("/logs/all", methods=["GET"])
def get_all_logs():
    try:
        http_request = HttpRequest()
        logs_handler = LogsHandler()

        http_response = logs_handler.get_all_logs(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_error(exception)
        return jsonify(http_response.body), http_response.status_code


@event_route_blueprint.route("/logs/tags/available", methods=["GET"])
def get_tags_available():
    return jsonify({"tags": tags_enum}), 200
