import re


def parse_vtt(path: str) -> list[tuple[str]]:
    with open(path, "r", encoding="utf-8-sig") as f:
        _lines: list[str] = f.readlines()

    lines: list[tuple[str]] = []
    starttime: str = ""
    text: str = ""

    for line in _lines:
        if re.match(r"^\n$", line):
            starttime = ""
            text = ""
        else:
            match: re.Match = re.match(r"^(\d{2}:\d{2}:\d{2}.\d{3}) -->.*", line)

            if match:
                starttime: str = match[1]
            else:
                text: str = re.match(r"(.*)\n", line)[1]
                if not starttime == "":
                    lines.append((starttime, text))
                    text = ""

    return lines
