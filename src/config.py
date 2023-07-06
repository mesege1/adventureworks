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