# RUAF Data Structuring

## Index
1. [Introduction](#introduction)
2. [Solution strategy](#solution-strategy)
3. [Repository structure](#repository-structure)


## Introduction
### Context
In Colombia, RUAF refers to the **Unique Registry of Affiliates**. It is a database managed by the Administrator of the Resources of the General System of Social Security in Health (ADRES). This registry contains information about individuals affiliated with the health system, including personal data and details about their affiliation and coverage.

RUAF enables data centralization, transparency, and control, manages affiliations, and facilitates administrative processes. Therefore, it is a key tool for managing the health system in Colombia, providing a comprehensive and up-to-date view of health system affiliation.

### Project Goal 
The starting point is a CSV file with unstructured RUAF data. The goal is to transform and structure this data based on the detailed instructions provided below and an accompanying [XLSX guide](data/raw/muestra_estructurada_RUAF.xlsx)

* Records begin with “¬-*-¬DATA”.
* Data is organized by sections, but these sections should not appear in the final table.
* If a record lacks information, add a “marca_sin_informacion” field with 0 for information present and 1 for no information.
* Fields should use snake_case notation

## Solution strategy

### First stage
An analysis of the raw data was conducted to identify structures and search patterns. Four repetitive sections of constant length were found. With this in mind, the objective of the first stage is to **transform the unstructured raw data into a structured format**, ensuring data uniqueness and consistency for future transformations.

![int pipeline](resources/int_pipeline.png)

The transformation process is carried out in the **intermediate pipeline**. This pipeline receives the raw file, reads it line by line, identifies the start pattern of each record, and extracts the data contained in each section. Using pandas, a dataframe is created with *base columns*, including f_consulta, key_fep, tipo_id_num, num_id, field, value and date

The function stores a CSV in the intermediate data stage to persist historical data and returns the dataframe for the next stage.

### Second stage
The goal at this stage is to perform transformation operations on the DataFrame to achieve the reference format. This stage is divided into three sub-stages: 

1. **Set up intermediate dataframe:** Receives the DataFrame produced by the intermediate pipeline. Normalizes the base columns, separates the first part of tipo_id_num from the second part, adds the second part to a new column called tipo_id_str, and finally creates the aux column as a concatenation of the field and value columns. The resulting aux column will be used in the subsequent sub-stages to generate the columns for the final structure.
The output of this function is: 
![first stage](resources/first_stage_mart_pipeline.png)
2. **Structuring dataframe:** Receives the DataFrame produced by the first sub-stage of the mart pipeline. It retains the base columns defined as a list in the data_dicts.py file, then uses the pivot_table function on the aux column to generate the new DataFrame structure. Finally, it reorders and renames the resulting columns based on the set_up_columns data dictionary provided in the data_dicts.py script.
The output of this function is:
![sec stage](resources/second_stage_mart_pipeline.png)
3. **Clean and transform data:** Receives the DataFrame produced by the second sub-stage of the mart pipeline. Performs data cleaning, transformation, and column generation operations to produce the final dataset.

## Repository structure

```linux

.
├── data                               # data storage in stages
│   │── raw
│   │── intermediate                   # data output from intermediate pipeline
│   └── mart
├── src                                # contains the work scripts
│   │── data_dicts.py                  # stores data structures for manage vars
│   │── functions.py                   # stores functions for column operation
│   │── int_pipeline.py                # transform unstructured data into dataframe
│   └── mart_pipeline.py
├── resources                          # contains no binary files for docs
├── .env                               # contains the environment variables
│
└── requirements.txt                   

```



