from cchardet import detect


def get_encoding(filepath):
    with open(filepath, "rb") as file:
        return detect(file.read())["encoding"]
