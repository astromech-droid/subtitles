import glob
import sys

import django

django.setup()

from app import cli  # noqa: E402


def main(argv):
    cmd = argv[1]

    if cmd == "download":
        extension = argv[2]

        if extension == "vtt":
            path = cli.download_vtt(url=argv[3], dirname=argv[4])

        elif extension == "xml":
            path = cli.download_xml(url=argv[3], path=argv[4])

        print(path)

    elif cmd == "load":
        cli.load_subs(path=argv[2], title=argv[3])

    elif cmd == "bulk_load":
        dirname = argv[2]
        pathes = glob.glob(f"{dirname}/*")

        for path in pathes:
            cli.load_subs(path=path, title=argv[3])


if __name__ == "__main__":
    try:
        main(sys.argv)

    except IndexError:
        print("[usage]")
        print("    download xml <url> <path>")
        print("    download vtt <url> <dirname>")
        print("    load <path> <title>")
        print("    bulk_load <dirname> <title>")
