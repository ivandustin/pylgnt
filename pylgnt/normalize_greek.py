from .filter_string import filter_string
from transliterate import translit


def normalize_greek(string):
    return filter_string(translit(string, "el"), 0x0391, 0x03A9)
