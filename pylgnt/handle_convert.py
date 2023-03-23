from pathlib import Path
from .constants import OT_NAME, NT_NAME
from .to_utf8 import to_utf8


def handle_convert(_):
    filepaths = [Path(OT_NAME), Path(NT_NAME)]
    for filepath in filepaths:
        to_utf8(filepath)
