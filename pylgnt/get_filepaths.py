from .constants.names import OLD, NEW
from pathlib import Path


def get_filepaths():
    return tuple(map(Path, [OLD, NEW]))
