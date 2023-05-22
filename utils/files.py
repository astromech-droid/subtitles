from pathlib import Path


def find(dirname: str, filename: str) -> str:
    pathes = list(Path(dirname).rglob(filename))
    if len(pathes) == 0:
        return ""
    else:
        return pathes[0]._str


def get_lines(path: str) -> list:
    with open(path, "r", encoding="utf-8-sig") as f:
        return f.readlines()
