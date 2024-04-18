from models.repository.logs_repository import LogsRepository

from models.settings.redis.redis_connection import redis_connection_handle
from models.repository.redis_repository import RedisRepository
from errors.error_types.http_not_found import HttpNotFoundError

from http_types.http_request import HttpRequest
from http_types.http_response import HttpResponse

from datetime import datetime

class LogsHandler:
    def __init__(self):
        self.__logs_repository = LogsRepository()

        self.__logs_redis_repository = RedisRepository(
            redis_connection_handle.connect()
        )

    def add_log(self, resqust: HttpRequest) -> HttpResponse:
        body = resqust.body
        params = resqust.param
        
        field = "add_log_" + datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f")

        self.__logs_redis_repository.insert_hash(params, field, body)

        return HttpResponse(
            status_code=201,
            body={"message": "Log added successfully"}
        )

    def get_log_by_id(self, request: HttpRequest) -> HttpResponse:
        log_id = request.param.get("log_id")
        log = self.__logs_repository.get_log_by_id(log_id)

        if not log:
            raise HttpNotFoundError("Log not found")

        return HttpResponse(
            status_code=200,
            body={
                "log_id": log.id,
                "tag": log.tag,
                "log": log.log,
                "created_at": log.created_at,
            }
        )

    def count_logs_by_tag(self, request: HttpRequest) -> HttpResponse:
        tag = request.param.get("tag")
        count = self.__logs_repository.count_logs_by_tag(tag)

        return HttpResponse(
            status_code=200,
            body={"count": count}
        )

    def get_all_logs(self, request: HttpRequest) -> HttpResponse:
        logs = self.__logs_repository.get_all_logs()

        return HttpResponse(
            status_code=200,
            body={
                "logs": [
                    {
                        "log_id": log.id,
                        "tag": log.tag,
                        "log": log.log,
                        "created_at": log.created_at,
                    }
                    for log in logs
                ]
            }
        )
