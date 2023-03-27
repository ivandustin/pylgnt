from pylgnt.get_dataframes import get_dataframes
from pylgnt.normalize import normalize


def main(_):
    dataframes = get_dataframes()
    dataframes = normalize(dataframes)
    for dataframe in dataframes:
        print(dataframe.info())
        print(dataframe)
