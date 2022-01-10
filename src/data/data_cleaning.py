def drop_columns(dataframe, columns):
    """Drop dataframe columns.

    Parameters
    ----------
    dataframe : pd.DataFrame
        DataFrame holding the data
    columns : list
        List of columns to drop
    """
    dataframe.drop(columns, axis=1, inplace=True)


def change_values(dataframe, columns_to_change):
    """Replace values of specified columns.

    Parameters
    ----------
    dataframe : pd.DataFrame
        DataFrame holding the data
    columns_to_change : dict
        Dictionary containing columns to change and values to replace
    """
    for column in columns_to_change.keys():
        for old_value, new_value in zip(
            columns_to_change[column]["old_values"],
            columns_to_change[column]["new_values"],
        ):
            dataframe.loc[dataframe[column] == old_value, column] = new_value
