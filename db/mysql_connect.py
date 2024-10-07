import os
from typing import Optional
import mysql.connector
from mysql.connector import errorcode
from dotenv import load_dotenv

load_dotenv(override=True)

config = {
    "user": os.getenv('USER'),
    "password": os.getenv('PASSWORD'),
    "host": os.getenv('HOST'),
    "database": os.getenv('DATABASE'),
    "port": os.getenv('PORT')
}

def connect_database() -> Optional[mysql.connector]:
    conn = None
    try:
        conn = mysql.connector.connect(**config)
        print("Connected!")
    except mysql.connector.Error as e:
        if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print(f"Unable to connect, check credentials...: {e}")
        else:
            print(f"error: {e}")

    if conn is not None:
        return conn
    else:
        print("The database connection was unsuccessful...")
