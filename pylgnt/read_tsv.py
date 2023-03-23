import pandas
from .get_encoding import get_encoding


def read_tsv(filepath):
    return pandas.read_csv(
        filepath, sep="\t", dtype=str, encoding=get_encoding(filepath)
    )
