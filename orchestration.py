import logging
import os
from dotenv import load_dotenv
import src.int_pipeline as int_pipeline
import src.mart_pipeline as mart_pipeline

logging.basicConfig(level=logging.INFO, format='%(levelname)s %(asctime)s - %(message)s')

def run_pipeline():
    
    load_dotenv()
    output_path = os.getenv("file_path_to_save_ruaf")
    
    try:
        logging.info("Starting the data extraction process")
        df = int_pipeline.extract_data_int_structure()
        logging.info("Data extraction complete")
        
        logging.info("Starting the data transformation process")
        ruaf = mart_pipeline.generate_structured_ruaf_matrix(df)
        logging.info("Data transformation complete")
        
        ruaf.to_excel(output_path, index=False)
        logging.info(f"Data saved successfully to {output_path}")
        
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    run_pipeline()
    