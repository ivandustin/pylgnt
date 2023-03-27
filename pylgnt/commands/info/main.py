from pylgnt.get_dataframes import get_dataframes


def main(_):
    dataframes = get_dataframes()
    for dataframe in dataframes:
        print(dataframe.info())
