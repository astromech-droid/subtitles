import json

import requests


def send_lines(url: str, lines: list[tuple[str]]):
    jsonstr = json.dumps({"lines": lines})
    return requests.post(url, jsonstr)
