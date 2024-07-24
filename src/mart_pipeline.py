import src.functions as fn
import src.data_dicts as dicts
import pandas as pd
import numpy as np

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

def clean_and_transform_data(df):
    """
    Clean and transform the DataFrame according to specific rules.

    Steps:
    1. Among the columns used for the pivot, we have num_id. This contains a composite value, so we will separate the data
    into the columns tipo_id_str_dup and num_id_val
    2. Handling duplicate columns that reference the same data with a coalesce function
    3. The column 'marca_sin_informacion' is created, setting it to 1 when num_id (ID from part 2 in S2, S3, and S4) is 
    equal to num_id_val (ID from the basic information section). If it is different, it indicates the presence of a 
    record that did not load information
    4.'sexo' data is embedded in some records of the segundo_apellido. The data was placed in the corresponding column
    
    Parameters:
    df (pd.DataFrame): The DataFrame to be cleaned and transformed.

    Returns:
    pd.DataFrame: The cleaned and transformed DataFrame.
    """
    try:
        # 1
        df = fn.duplicate_column_next_to_original(df, 'nume_id')
        df = fn.split_columns_by_delimiter(df, 'nume_id', ' ', 0).rename(columns = {'nume_id':'tipo_id_str_dup'})
        df = fn.split_columns_by_delimiter(df, 'nume_id_duplicates', ' ', 1).rename(columns = {'nume_id_duplicates':'num_id_val'})
        # 2
        df = fn.coalesce_columns(df, 'f_afiliacion_salud', 'f_de_afiliacion_salud')
        df = fn.coalesce_columns(df, 'tipo_id_str', 'tipo_id_str_dup')
        # 3
        df['marca_sin_informacion'] = np.where((df['num_id'] == df['num_id_val']), 0, 1)
        df.loc[df['evaluacion_marca'] == 'La consulta no fue exitosa', 'key_fep'] = np.nan
        # 4 
        df.loc[df['segundo_apellido'].str.len() == 1, 'sexo'] = df['segundo_apellido']
        df.loc[df['segundo_apellido'].str.len() == 1, 'segundo_apellido'] = np.nan
        
        pos = df.columns.get_loc('est_afiliacion_cf')
        df.insert(pos + 1, 'municipio_laboral_cf', None) # add missing column
        df_cleaned = df.drop(columns=['num_id_val','evaluacion_marca']) # auxiliary columns are removed
        
    except KeyError as e:
        raise KeyError(f"column error: {e}")
    except Exception as e:
        raise RuntimeError(f"In clean_and_transform_data function, an error occurred during df processing: {e}")
    
    return df_cleaned

def generate_structured_ruaf_matrix(df):
    df_processed = set_up_int_data(df)
    pivot_df = structuring_dataframe(df_processed)
    df_cleaned = clean_and_transform_data(pivot_df)
    
    return df_cleaned
