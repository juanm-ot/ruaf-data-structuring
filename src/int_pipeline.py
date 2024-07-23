import os
from dotenv import load_dotenv
import functions as fn
import pandas as pd


def extract_data_int_structure():
    """
    Extracts and processes data from a specified file into a structured DataFrame and saves it as a CSV.

    Steps:
    1. Loads environment variables for file paths.
    2. Reads the input file line by line.
    3. Processes each line to extract relevant data fields.
    4. Creates a DataFrame from the extracted data.
    5. Saves the DataFrame to a specified CSV file path.
    
    Returns:
    pd.DataFrame: The processed DataFrame.
    """
    load_dotenv()
    file_path = os.getenv("file_path_to_read")
    save_path = os.getenv("file_path_to_save_int")


    with open(file_path, 'r', encoding='latin1') as file:
        lines = file.readlines()

    data = []
    key_fep = None
    f_consulta = None

    for line in lines:
        line = line.strip()
        
        if line.startswith('¬-*-¬DATA'):
            parts = line.split(';;')
            f_consulta = fn.format_date(parts[1])
        elif line.startswith('¬-*-¬ID'):
            parts = line.split(';')
            key_fep = parts[1]
        else:
            parts = line.split(';')
            if len(parts) == 6:
                row = {
                    'f_consulta': f_consulta,
                    'key_fep': key_fep,
                    'tipo_id_num': parts[0],
                    'num_id': parts[1],
                    'field': parts[2],
                    'name': parts[3],
                    'value': parts[4],
                    'date': parts[5]
                }
            elif len(parts) == 5:
                row = {
                    'f_consulta': f_consulta,
                    'key_fep': key_fep,
                    'tipo_id_num': parts[0],
                    'num_id': parts[1],
                    'field': parts[2],
                    'name': parts[3],
                    'value': '',
                    'date': parts[4]
                }
            elif len(parts) == 4:
                row = {
                    'f_consulta': f_consulta,
                    'key_fep': key_fep,
                    'tipo_id_num': parts[0],
                    'num_id': parts[1],
                    'field': '',
                    'name': 'request',
                    'value': parts[2],
                    'date': parts[3]
                }
            data.append(row)

    df = pd.DataFrame(data)
    df.to_csv(save_path , index=False)
    
    return df

if __name__ == "__main__":
    extract_data_int_structure()