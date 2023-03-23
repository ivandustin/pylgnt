def get_nan(dataframe):
    return dataframe[dataframe.isnull().any(axis=1)]
