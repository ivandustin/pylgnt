from pandas import Series, DataFrame
from pylgnt.get_dataframes import get_dataframes
from pylgnt.normalize import normalize


def main(args):
    dataframes = get_dataframes()
    if args.normalize:
        dataframes = normalize(dataframes)
    else:
        dataframes = rename_columns(dataframes)
    series = tuple([dataframe["word"] for dataframe in dataframes])
    for words in series:
        print(table(words))


def rename_columns(dataframes):
    mapping = {"Hebrew": "word", "Greek": "word"}
    return tuple([dataframe.rename(columns=mapping) for dataframe in dataframes])


def table(words):
    letters = get_letters(words)
    codepoints = letters.apply(ord).apply(hex)
    return DataFrame({"letter": letters, "codepoint": codepoints})


def get_letters(words):
    words = words.dropna()
    letters = Series([letter for word in words for letter in word])
    return Series(letters.sort_values().unique())
