import re


def parse(path: str) -> list[tuple[str]]:
    with open(path, "r", encoding="utf-8-sig") as f:
        lines: list[str] = f.readlines()

    _lines: list[tuple[str]] = []
    text_buffer: list[str] = []
    starttime_buffer: str = ""

    for line in lines:
        match_st: re.Match = re.match(r"^(\d{2}:\d{2}:\d{2}.\d{3}) -->.*", line)

        if match_st:
            starttime: str = match_st[1]

            if starttime_buffer == "":
                text_buffer.clear()

            else:
                _lines.append((starttime_buffer, " ".join(text_buffer)))
                text_buffer.clear()

            starttime_buffer = starttime

        else:
            match_txt: re.Match = re.match(r"(.+)\n", line)
            if match_txt:
                text: str = match_txt[1]
                text_buffer.append(text)

    _lines.append((starttime_buffer, " ".join(text_buffer)))

    return _lines
