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
        pathes = sorted(glob.glob(f"{dirname}/*"))

        for path in pathes:
            cli.load_subs(path=path, title=argv[3])

    elif cmd == "bulk_reload":
        dirname = argv[2]
        pathes = sorted(glob.glob(f"{dirname}/*"))

        for i, path in enumerate(pathes):
            if i == 0:
                cli.reload_subs(path=path, title=argv[3])
            else:
                cli.load_subs(path=path, title=argv[3])

    elif cmd == "send":
        dirname = argv[2]
        pathes = sorted(glob.glob(f"{dirname}/*"))
        lines = []
        for path in pathes:
            lines += cli.read_lines(path)

        cli.send_lines(url=argv[3], lines=lines)


if __name__ == "__main__":
    try:
        main(sys.argv)

    except IndexError:
        print("[usage]")
        print("    download xml <url> <path>")
        print("    download vtt <url> <dirname>")
        print("    load <path> <title>")
        print("    bulk_load <dirname> <title>")
        print("    bulk_reload <dirname> <title>")
        print("    send <dirname>")
