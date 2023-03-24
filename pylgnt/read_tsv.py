import pandas
from .get_encoding import get_encoding


def read_tsv(filepath):
    return pandas.read_csv(
        filepath, sep="\t", dtype="string", encoding=get_encoding(filepath)
    )
