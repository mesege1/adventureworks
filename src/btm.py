import pandas as pd
import psycopg2
from psycopg2 import OperationalError
import pathlib
import sqlalchemy
#import pyodbc

import os
from dotenv import load_dotenv

load_dotenv()

POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
POSTGRES_DATABASE = os.getenv('POSTGRES_DATABASE')

def create_connection():
    connection = None
    try:
        connection = psycopg2.connect(
            database=POSTGRES_DATABASE,
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD,
            host=POSTGRES_HOST,
            port=POSTGRES_PORT,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection


def convert_sql_to_xlsx(sql_in, xlsx_out, xlsx_name=None):
    """
    Runs query in given .sql file, stores result as .xlsx file.

    Parameters:
        sql_in (str): relative filepath to .sql file
        xlsx_out (str): relative filepath to directory where .xlsx will be stored
        xlsx_name (str or None): If not None, file named xlsx_name.xlsx
                                 If None, file named same as sql_in

    Returns:
        None
    """
    if xlsx_name is None:
        xlsx_name = sql_in.split("/")[-1].replace('.sql','')
        
    conn = create_connection()
    
    with open(sql_in, "r") as sql_file:
        query = sql_file.read()

    df = pd.read_sql_query(query, conn)

    conn.close()
    return df.to_excel(f"{xlsx_out}/{xlsx_name}.xlsx") 
    

def convert_directory_of_queries(sql_in_dir, xlsx_out_dir):
    """
    Runs each query in sql_in_dir directory,
        stores each result as .xlsx in xlsx_out_dir.

    Parameters:
        sql_in_dir (str): relative filepath to directory
                          containing .sql files
        xlsx_out_dir (str): relative filepath to directory
                            where .xlsx will be stored
                            files named same as sql_in

    Returns:
        None
    """
    directory = sql_in_dir
 
    # iterate over files in
    # that directory
    for filename in os.scandir(directory):
        if filename.is_file():
            new_file = filename.path
        convert_sql_to_xlsx(new_file, xlsx_out_dir)
        #convert_sql_to_xlsx(file, xlsx_out_dir)
    

def convert_sql_to_xlsx_from_cli():
    """
    Converts directory of sql queries to xlsx from CLI.
    """
    pass

if __name__ == "__main__":
    print(POSTGRES_DATABASE)
    #convert_sql_to_xlsx("sql_queries/hr_q1.sql", "hr_q1")
    convert_directory_of_queries('sql_queries/', 'excel_reports/')

    