from remote_setup import refresh_docker_env
# Assuming your previous DB functions are in db_utils.py
from db_utils import run_admin_command, setup_db 

def main():
    # Phase 0: Reset the Remote Docker Environment
    if not refresh_docker_env():
        print("Aborting: Docker setup failed.")
        return

    # Phase 1: Create the specific database (The "Admin" step)
    # This connects to 'postgres' and runs 'CREATE DATABASE...'
    try:
        run_admin_command('01_create_database.sql')
    except Exception as e:
        print(f"DB Creation Note: {e}")

    # Phase 2: Build tables and insert data
    # This connects to the DB name defined in your .env
    print("Building schema and loading data...")
    setup_db()

    print("\n--- Setup Complete ---")
    print("Database: http://[REMOTE_IP]:5432")
    print("Adminer UI: http://[REMOTE_IP]:8080")

if __name__ == "__main__":
    main()