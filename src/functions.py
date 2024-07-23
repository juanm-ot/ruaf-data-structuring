import pandas as pd
import unidecode
import numpy as np


def duplicate_column_next_to_original(df, columna):
    """
    Duplicate a specified column in a DataFrame, placing the duplicated column 
    immediately after the original column.

    Parameters:
    df (pd.DataFrame): The DataFrame containing the column to be duplicated.
    columna (str): The name of the column to duplicate.

    Returns:
    pd.DataFrame: The DataFrame with the duplicated column added.
    """
    pos = df.columns.get_loc(columna) # Find the position of the original column
    df.insert(pos + 1, f"{columna}_duplicates", df[columna])
    return df

def format_date(date_str):
    """
    Convert a date string to a specific format.

    This function takes a date string in the format '%Y-%m-%d %H:%M:%S' and converts it to a 
    formatted string in the format '%d/%m/%Y %H:%M'.

    Args:
    date_str (str): The date string to be converted. It should be in the format '%Y-%m-%d %H:%M:%S'.

    Returns:
    str: The formatted date string in the format '%d/%m/%Y %H:%M'.
    """
    date_obj = pd.to_datetime(date_str, format='%Y-%m-%d %H:%M:%S')
    return date_obj.strftime('%d/%m/%Y %H:%M')

def normalize_column(df, column):
    """
    Clean data in a specific column of a DataFrame by normalizing text values.

    This function applies several transformations to the values in the specified column:
    - Converts the values to strings.
    - Removes accents from characters using `unidecode`.
    - Converts all characters to lowercase.
    - Replaces spaces with underscores.

    Args:
    df (pd.DataFrame): The DataFrame containing the column to be cleaned.
    columna (str): The name of the column to be cleaned.

    Returns:
    pd.DataFrame: The DataFrame with the specified column cleaned according to the transformations.
    """
    df[column] = df[column].apply(lambda x: unidecode.unidecode(str(x)).lower().replace(' ', '_'))
    return df

def reorder_and_rename_columns(df, base_columns, rename_columns):
    """
    Adjust the columns of a DataFrame by maintaining fixed columns and renaming others 
    according to a provided dictionary.

    Parameters:
    df (pd.DataFrame): The DataFrame to be adjusted.
    columnas_fijas (list of str): List of column names to be retained in their original form.
    columnas_a_renombrar (dict): Dictionary mapping current column names to new names for renaming.

    Returns:
    pd.DataFrame: The adjusted DataFrame with fixed columns retained and other columns renamed 
                  and rearranged according to the provided dictionary.
    """
    df_base_columns = df[base_columns] # Maintain the fixed columns
    df_rename_columns = df.rename(columns=rename_columns) # Rename and select columns
    df_rename_columns = df_rename_columns[list(rename_columns.values())]
    
    df_structured = pd.concat([df_base_columns, df_rename_columns], axis=1)
    return df_structured

def split_columns_by_delimiter(df, column, delimiter, position):
    """
    Split the specified column in a DataFrame into multiple values based on a delimiter, 
    and keep only the value at the specified position.

    Parameters:
    df (pd.DataFrame): The DataFrame containing the column to be split.
    columna (str): The name of the column to split.
    delimitador (str): The delimiter used to split the column values.
    posicion (int): The position of the value to keep from the split results.

    Returns:
    pd.DataFrame: The DataFrame with the specified column updated to only include 
                  the value at the specified position after splitting.
    """
    df[column] = df[column].str.split(delimiter).str[position]
    return df






