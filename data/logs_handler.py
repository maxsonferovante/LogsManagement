from models.repository.logs_repository import LogsRepository
from errors.error_types.http_not_found import HttpNotFoundError

from http_types.http_request import HttpRequest
from http_types.http_response import HttpResponse


class LogsHandler:
    def __init__(self):
        self.__logs_repository = LogsRepository()

    def add_log(self, resqust: HttpRequest) -> HttpResponse:
        body = resqust.body
        self.__logs_repository.add_log(body)

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
