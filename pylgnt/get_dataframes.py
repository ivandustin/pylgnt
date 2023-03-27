from .get_filepaths import get_filepaths
from .read_tsv import read_tsv


def get_dataframes():
    return tuple(map(read_tsv, get_filepaths()))
