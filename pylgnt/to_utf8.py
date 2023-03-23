from tempfile import TemporaryDirectory
from pathlib import Path
from shutil import copyfileobj, move
from .get_encoding import get_encoding


def to_utf8(filepath):
    with TemporaryDirectory() as tempdir:
        tempdir = Path(tempdir)
        tempfile = tempdir / filepath.name
        encoding = get_encoding(filepath)
        with open(filepath, "r", encoding=encoding) as source:
            with open(tempfile, "w", encoding="utf-8") as destination:
                copyfileobj(source, destination)
        move(tempfile, filepath)
