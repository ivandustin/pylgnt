from pathlib import Path
from .constants.names import OLD, NEW


def get_filepaths():
    return tuple(map(Path, [OLD, NEW]))
