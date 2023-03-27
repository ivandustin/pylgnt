from .decompose import decompose


def filter_string(string, a, z):
    return "".join(
        filter(lambda character: a <= ord(character) <= z, decompose(string))
    )
