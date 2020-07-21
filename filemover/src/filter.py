from typing import Set


class FileFilter:

    def __init__(self, *args):
        self.file_endings: Set[str] = set()
        for ext in args:
            self.file_endings.add(ext)

    def __contains__(self, item):
        return item in self.file_endings

    def __str__(self) -> str:
        return ",".join(self.file_endings)
