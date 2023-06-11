import os

from subtitles import settings


class Merger:
    def __init__(self):
        pass

    def merge(self, dirname_src, path_dst: str) -> str:
        filenames: str = sorted(os.listdir(dirname_src))

        if os.path.exists(path_dst):
            os.remove(path_dst)

        for filename in filenames:
            if filename != settings.DEFAULT_TXT_FILENAME:
                path_src: str = os.path.join(dirname_src, filename)

                with open(path_src, "r") as f:
                    text = f.read()

                with open(path_dst, "a") as g:
                    g.write(text)

        return path_dst
