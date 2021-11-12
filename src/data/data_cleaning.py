def drop_columns(dataframe, columns):
    dataframe.drop(columns, axis=1, inplace=True)


def change_values(dataframe, columns_to_change):
    for column in columns_to_change.keys():
        for old_value, new_value in zip(
            columns_to_change[column]["old_values"],
            columns_to_change[column]["new_values"],
        ):
            dataframe.loc[dataframe[column] == old_value, column] = new_value
