from unicodedata import normalize
from functools import partial

decompose = partial(normalize, "NFD")
