import os

from subtitles import settings


class Merger:
    def __init__(self):
        pass

    def merge(self, dirname_src, path_dst: str) -> str:
        filenames: str = sorted(os.listdir(dirname_src))

        for i, filename in enumerate(filenames):
            if filename != settings.DEFAULT_TXT_FILENAME:
                path_src: str = os.path.join(dirname_src, filename)

                with open(path_src, "r") as f:
                    text = f.read()

                if i == 0:
                    with open(path_dst, "w") as g:
                        g.write(text)

                else:
                    with open(path_dst, "a") as g:
                        g.write(text)

        return path_dst
