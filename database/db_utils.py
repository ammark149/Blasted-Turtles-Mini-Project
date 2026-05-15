import os
import psycopg2
from psycopg2 import errors
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from dotenv import load_dotenv

load_dotenv()

def get_connection(dbname=None):
    """Connects to a specific DB, or the default from .env if none provided."""
    return psycopg2.connect(
        host=os.getenv("POSTGRES_HOST"),
        port=os.getenv("DB_PORT"),
        # If dbname is passed, use it; otherwise use the .env default
        database=dbname or os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )

def run_admin_command(file_path):
    conn = get_connection(dbname="postgres")
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    
    try:
        with open(file_path, 'r') as file:
            cur.execute(file.read())
        print("Database created successfully.")
    except psycopg2.errors.DuplicateDatabase:
        print("Database already exists. Moving to schema setup...")
    except Exception as e:
        print(f"Unexpected error creating database: {e}")
    finally:
        cur.close()
        conn.close()

def setup_db():
    # --- STEP 1: CREATE THE DATABASE ---
    # We MUST connect to 'postgres' (the default) to create a new DB
    try:
        print("Connecting to 'postgres' to create the database...")
        conn = get_connection(dbname="postgres")
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()
        
        with open('01_create_database.sql', 'r') as file:
            cur.execute(file.read())
        
        cur.close()
        conn.close()
     
    except Exception as e:
        print(f"Admin Step Note: {e}")

    # --- STEP 2: CREATE TABLES & DATA ---
    # Now we open a FRESH connection to the ACTUAL database
    # Make sure your .env POSTGRES_DB matches the name in your SQL script!
    try:
        print(f"Connecting to target database: {os.getenv('POSTGRES_DB')}...")
        conn = get_connection() # Uses the DB name from your .env
        cur = conn.cursor()

        sql_files = ['02_create_tables.sql', '03_insert_data.sql']
        for file_path in sql_files:
            print(f"Executing {file_path}...")
            with open(file_path, 'r') as file:
                cur.execute(file.read())
        
        conn.commit()
        print("Tables and data loaded successfully.")

    except Exception as e:
        if conn:
            conn.rollback()
        print(f"Error loading schema/data: {e}")
    finally:
        if conn:
            cur.close()
            conn.close()

if __name__ == "__main__":
    setup_db()