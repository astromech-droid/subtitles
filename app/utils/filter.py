import re


def merge_tail(lines) -> list[tuple[str]]:
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


def merge_head(lines) -> list[tuple[str]]:
    _lines: list[tuple[str]] = []

    for starttime, text in lines:
        if len(_lines) == 0:
            # 一行目が小文字から始まる場合にIndexErrorを出さないため
            _lines.append((starttime, text))

        elif re.match(r"^[a-z]", text):
            _starttime, _text = _lines.pop()
            _lines.append((_starttime, f"{_text} {text}"))

        else:
            _lines.append((starttime, text))

    return _lines


def remove_tag(lines) -> list[tuple[str]]:
    _lines = []

    for line in lines:
        timestamp, text = line
        _text = text.replace("<i>", "").replace("</i>", "").strip()
        _lines.append((timestamp, _text))

    return _lines


def filter(lines) -> list[tuple[str]]:
    lines = remove_tag(lines)
    lines = merge_tail(lines)
    lines = merge_head(lines)

    return lines
