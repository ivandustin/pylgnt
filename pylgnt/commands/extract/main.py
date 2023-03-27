from pathlib import Path
from pandas import concat
from pylgnt.constants.mappings.book.old import MAPPING as OLD_MAPPING
from pylgnt.constants.mappings.book.new import MAPPING as NEW_MAPPING
from pylgnt.get_dataframes import get_dataframes
from pylgnt.normalize import normalize


def main(args):
    directory = Path(args.directory)
    dataframes = get_dataframes()
    dataframes = normalize(dataframes)
    dataframes = add_book_number(dataframes)
    dataframes = add_testament(dataframes)
    dataframe = concat(dataframes)
    columns = ["chapter", "verse", "word"]
    save(dataframe, directory, columns)


def add_book_number(dataframes):
    mappings = [OLD_MAPPING, NEW_MAPPING]
    titles = [mapping.values() for mapping in mappings]
    mappings = [dict(zip(titles, range(len(titles)))) for titles in titles]
    for mapping, dataframe in zip(mappings, dataframes):
        dataframe["book_number"] = dataframe["book"].map(mapping) + 1
    return dataframes


def add_testament(dataframes):
    for testament, dataframe in zip(["old", "new"], dataframes):
        dataframe["testament"] = testament
    return dataframes


def save(dataframe, directory, columns):
    groups = dataframe.groupby(["testament", "book_number", "book"])
    for (testament, book_number, book), group in groups:
        filename = f"{book_number:02}-{book}.csv".replace(" ", "-").lower()
        filepath = directory / testament / filename
        filepath.parent.mkdir(parents=True, exist_ok=True)
        group[columns].to_csv(filepath, index=False)
    return dataframe
