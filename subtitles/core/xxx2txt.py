from abc import ABCMeta, abstractclassmethod


class Xxx2txt(metaclass=ABCMeta):
    @abstractclassmethod
    def parse(lines: list[str]) -> list[tuple[str]]:
        pass

    @abstractclassmethod
    def read(path: str) -> list[str]:
        pass

    @abstractclassmethod
    def write(path: str, lines: list[tuple[str]]) -> None:
        pass
