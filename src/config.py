import os
from dotenv import load_dotenv

load_dotenv()

POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
POSTGRES_DATABASE = os.getenv('POSTGRES_DATABASE')

if __name__ == "__main__":
    print(
        POSTGRES_PASSWORD,
        POSTGRES_USER,
        POSTGRES_HOST,
        POSTGRES_PORT,
        POSTGRES_DATABASE
    )

"""
import psycopg2 as pg2
conn = pgs2.connect(
    dbname=POSTGRES_DATABASE,
    user=POSTGRES_USER,
    password=POSTGRES_PASSWORD,
    host=POSTGRES_HOST,
    port=POSTGRES_PORT
)

query = "
fill 
in 
your
query
here"


cur = conn.cursor()

cur.execute(query)

for row in cur:
    print(row)


query_df = pd.readsql(
    query,
    conn)
display(query_df)

query_df.to_excel(
    "demo.xlsx
)

"""