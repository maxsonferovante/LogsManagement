from typing import Dict


class HttpResponse:
    status_code: int
    body: Dict

    def __init__(self, body: Dict, status_code: int) -> None:
        self.body = body
        self.status_code = status_code
