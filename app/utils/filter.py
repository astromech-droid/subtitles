import re


def merge(lines) -> list[tuple[str]]:
    _lines: list[tuple[str]] = []
    starttime_buffer: list[str] = []
    text_buffer: list[str] = []

    for starttime, text in lines:
        text_buffer.append(text)

        if len(starttime_buffer) == 0:
            starttime_buffer.append(starttime)

        if not re.match(r".*[a-z]$|.*,$", text):
            text: str = " ".join(text_buffer)
            _lines.append((starttime_buffer.pop(), text))
            text_buffer.clear()
            starttime_buffer.clear()

    return _lines
