from pylgnt.constants.mappings.book.old import MAPPING as OLD_MAPPING
from pylgnt.constants.mappings.book.new import MAPPING as NEW_MAPPING
from pylgnt.codepoints.fix import fix as fix_codepoint


def normalize(dataframes):
    return tuple(map(normalize_dataframe, dataframes))


def normalize_dataframe(dataframe):
    pipeline = [
        rename_columns,
        remove_null_positions,
        filter_columns,
        trim,
        fix_codepoints,
        rename_book,
        remove_nulls,
        reindex,
        retype,
    ]
    return apply(pipeline, dataframe)


def apply(pipeline, dataframe):
    for function in pipeline:
        dataframe = function(dataframe)
    return dataframe


def rename_columns(dataframe):
    columns = {
        "Book": "book",
        "Chap": "chapter",
        "Vs": "verse",
        "Hebrew": "word",
        "Greek": "word",
        "Book Word position": "position",
    }
    return dataframe.rename(columns=columns)


def remove_null_positions(dataframe):
    return dataframe[dataframe["position"].notnull()]


def filter_columns(dataframe):
    columns = ["book", "chapter", "verse", "word"]
    return dataframe[columns]


def trim(dataframe):
    return dataframe.transform(lambda series: series.str.strip())


def fix_codepoints(dataframe):
    dataframe["word"] = dataframe["word"].map(fix_codepoint)
    return dataframe


def rename_book(dataframe):
    dataframe["book"] = dataframe["book"].map(OLD_MAPPING | NEW_MAPPING)
    return dataframe


def remove_nulls(dataframe):
    return dataframe.dropna()


def reindex(dataframe):
    return dataframe.reset_index(drop=True)


def retype(dataframe):
    types = {
        "book": "string",
        "chapter": "int",
        "verse": "int",
        "word": "string",
    }
    return dataframe.astype(types)
