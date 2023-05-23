import os
from pathlib import Path


def find_path(dirname: str, filename: str) -> str:
    pathes = list(Path(dirname).rglob(filename))
    if len(pathes) == 0:
        return ""
    else:
        return pathes[0]._str


def get_lines(path: str) -> list:
    with open(path, "r", encoding="utf-8-sig") as f:
        return f.readlines()


def save_text(text: str, path: str) -> bool:
    dirname = os.path.dirname(path)

    if not os.path.exists(dirname):
        os.makedirs(dirname)

    if text == "":
        return False

    else:
        with open(path, "w") as f:
            f.write(text)
            return True
