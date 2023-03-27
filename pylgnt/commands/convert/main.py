from pylgnt.get_filepaths import get_filepaths
from pylgnt.to_utf8 import to_utf8


def main(_):
    filepaths = get_filepaths()
    for filepath in filepaths:
        to_utf8(filepath)
