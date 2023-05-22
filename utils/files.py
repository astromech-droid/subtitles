from pathlib import Path


def find(dirname: str, filename: str) -> str:
    pathes = list(Path(dirname).rglob(filename))
    if len(pathes) == 0:
        return ""
    else:
        return pathes[0]._str
