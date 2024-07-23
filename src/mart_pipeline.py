import os
from dotenv import load_dotenv
import functions as fn
import data_dicts as dicts
import int_pipeline
import pandas as pd


df = int_pipeline.extract_data_int_structure()

def set_up_int_data(df):
    """
    Process the intermediate dataframe by normalizing columns, duplicating and splitting columns 
    to generate tipo_id_str from tipo_id_num, and mapping field codes to names 
    for create aux var for unify field and name.

    Parameters:
    df (pd.DataFrame): The DataFrame to be processed.

    Returns:
    pd.DataFrame: The processed DataFrame.
    """
    try:
        df = fn.normalize_column(df, 'name')
        df = fn.normalize_column(df, 'field')
        df = fn.duplicate_column_next_to_original(df, 'tipo_id_num')
        df = fn.split_columns_by_delimiter(df, 'tipo_id_num_duplicates', '|', 1).rename(columns={'tipo_id_num_duplicates': 'tipo_id_str'})
        df = fn.split_columns_by_delimiter(df, 'tipo_id_num', '|', 0)
        df['field'] = df['field'].replace(dicts.field_code)
        df['aux'] = df['field'] + '/' + df['name']
    except KeyError as e:
        raise KeyError(f"column error: {e}")
    except Exception as e:
        raise RuntimeError(f"In set_up_int_data function, an error occurred during df processing: {e}")

    return df

def structuring_dataframe(df):
    """
    Restructure the DataFrame by pivoting it based on specified columns and then reordering and renaming the columns.

    Parameters:
    df (pd.DataFrame): The DataFrame to be structured.

    Returns:
    pd.DataFrame: The restructured DataFrame with pivoted data, reordered, and renamed columns.
    """
    try:
        df_pivot = df.pivot_table(
            index=['f_consulta', 'key_fep', 'tipo_id_num', 'tipo_id_str', 'num_id'], 
            columns='aux', 
            values='value', 
            aggfunc='first'
        ).reset_index()
        df_structured = fn.reorder_and_rename_columns(df_pivot, dicts.base_columns, dicts.set_up_columns)
    except KeyError as e:
        raise KeyError(f"column error: {e}")
    except Exception as e:
        raise RuntimeError(f"In structuring_dataframe function, an error occurred during df processing: {e}")
    
    return df_structured

df_processed = set_up_int_data(df)
pivot_df = structuring_dataframe(df_processed)
pivot_df.to_csv('test.csv' , index=False)

