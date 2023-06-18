import sys

from app import cli


def main(argv):
    cmd = argv[1]

    if cmd == "download":
        extension = argv[2]

        if extension == "vtt":
            cli.download_vtt(url=argv[3], dirname=argv[4])

        elif extension == "xml":
            cli.download_xml(url=argv[3], path=argv[4])


if __name__ == "__main__":
    try:
        main(sys.argv)

    except IndexError:
        print("[usage]")
        print("    download xml <url> <path>")
        print("    download vtt <url> <dirname>")
