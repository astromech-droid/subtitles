import os
import re


def parse(lines: list[str]) -> list[tuple[str]]:
    _lines: list[tuple[str]] = []
    text_buffer: list[str] = []
    starttime_buffer: str = ""

    for line in lines:
        if re.match(r"^\d{2}:\d{2}:\d{2}.\d{3} -->.*", line):
            starttime: str = re.match(r"^(\d{2}:\d{2}:\d{2}.\d{3}) -->.*", line)[1]

            if starttime_buffer == "":
                text_buffer.clear()

            else:
                _lines.append((starttime_buffer, " ".join(text_buffer)))
                text_buffer.clear()

            starttime_buffer = starttime

        else:
            if re.match(r"(.+)\n", line):
                text: str = re.match(r"(.+)\n", line)[1]
                text_buffer.append(text)

    _lines.append((starttime_buffer, " ".join(text_buffer)))

    return _lines


def read(path: str) -> list[str]:
    with open(path, "r", encoding="utf-8-sig") as f:
        lines: list[str] = f.readlines()

    return parse(lines)


def save(path: str, lines: list[tuple[str]]) -> None:
    dirname: str = os.path.dirname(path)

    if not os.path.exists(dirname):
        os.makedirs(dirname)

    with open(path, "w") as f:
        for starttime, text in lines:
            f.write(f"{starttime}: {text}\n")
