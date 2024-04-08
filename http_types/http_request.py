from typing import Dict


class HttpRequest:
    body: Dict
    param: Dict

    def __init__(self, body: Dict = None, param: Dict = None) -> None:
        self.body = body
        self.param = param
