from pathlib import Path
from pandas import concat
from .constants import OT_NAME, NT_NAME
from .book_titles import book_titles
from .read_tsv import read_tsv
from .get_nan import get_nan


def handle_extract(_):
    filepaths = [Path(OT_NAME), Path(NT_NAME)]
    dataframes = [read_tsv(filepath) for filepath in filepaths]
    columns = ["Book", "Chap", "Vs", "Book Word position"]
    columns = [
        columns + ["OT Word position", "Hebrew"],
        columns + ["NT Word position", "Greek"],
    ]
    dataframes = [dataframe[columns] for dataframe, columns in zip(dataframes, columns)]
    dataframes = [
        dataframe.transform(lambda series: series.str.strip())
        for dataframe in dataframes
    ]
    dataframes = [dataframe.dropna() for dataframe in dataframes]
    dataframes = [
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
    dataframes = [
        dataframe[["book", "chapter", "verse", "word"]] for dataframe in dataframes
    ]
    for dataframe in dataframes:
        dataframe["book"] = dataframe["book"].map(book_titles).astype("string")
    dataframe = concat(dataframes)
    print(dataframe.head())
    print(dataframe.tail())
    print(dataframe.info())
    print(len(dataframe["book"].unique()))
