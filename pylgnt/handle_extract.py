from pathlib import Path
from pandas import concat
from .book_mappings import old as old_mapping, new as new_mapping
from .constants import OT_NAME, NT_NAME
from .read_tsv import read_tsv


def handle_extract(args):
    directory = Path(args.directory)
    filepaths = [Path(OT_NAME), Path(NT_NAME)]
    dataframes = get_dataframes(filepaths)
    dataframes = filter_columns(dataframes)
    dataframes = trim(dataframes)
    dataframes = dropna(dataframes)
    dataframes = normalize_columns(dataframes)
    dataframes = filter_normal_columns(dataframes)
    dataframes = normalize_book(dataframes)
    dataframes = add_book_number(dataframes)
    dataframes = add_testament(dataframes)
    dataframe = concat(dataframes)
    columns = ["chapter", "verse", "word"]
    save(dataframe, directory, columns)


def get_dataframes(filepaths):
    return [read_tsv(filepath) for filepath in filepaths]


def filter_columns(dataframes):
    columns = ["Book", "Chap", "Vs", "Book Word position"]
    columns = [
        columns + ["OT Word position", "Hebrew"],
        columns + ["NT Word position", "Greek"],
    ]
    return [dataframe[columns] for dataframe, columns in zip(dataframes, columns)]


def trim(dataframes):
    return [
        dataframe.transform(lambda series: series.str.strip())
        for dataframe in dataframes
    ]


def dropna(dataframes):
    return [dataframe.dropna() for dataframe in dataframes]


def normalize_columns(dataframes):
    return [
        dataframe.rename(
            columns={
                "Book": "book",
                "Chap": "chapter",
                "Vs": "verse",
                "Hebrew": "word",
                "Greek": "word",
            }
        )
        for dataframe in dataframes
    ]


def filter_normal_columns(dataframes):
    return [dataframe[["book", "chapter", "verse", "word"]] for dataframe in dataframes]


def normalize_book(dataframes):
    for mapping, dataframe in zip([old_mapping, new_mapping], dataframes):
        dataframe["book"] = dataframe["book"].map(mapping).astype("string")
    return dataframes


def add_book_number(dataframes):
    mappings = [old_mapping, new_mapping]
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
