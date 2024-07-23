import pandas as pd
import unidecode
import numpy as np

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




