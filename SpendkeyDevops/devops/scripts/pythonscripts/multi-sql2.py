import os
import pyodbc
from glob import glob
import argparse

servers = [
    {
        'server': 'sqlsrv-ne-dev-spendkey1.database.windows.net',
        'database': 'sqldb-ne-dev-sk',
        'username': 'CloudSA697e03f6',
        'password': 'wpxfTCd?K3R+73U~CPWo@TNMBt3@%',
    },
    {
        'server': 'sqlsrv-ne-dev-spendkey1.database.windows.net',
        'database': 'sqldb-ne-test2-spendkey',
        'username': 'CloudSA697e03f6',
        'password': 'wpxfTCd?K3R+73U~CPWo@TNMBt3@%',
    },
    {
        'server': 'sqlsrv-ne-dev-spendkey1.database.windows.net',
        'database': 'sqldb-ne-reckittdev-spendkey',
        'username': 'CloudSA697e03f6',
        'password': 'wpxfTCd?K3R+73U~CPWo@TNMBt3@%',
    },
    
]

# Directory containing the SQL scripts
script_directory = os.path.join(os.getcwd(), 'sql_scripts')

# Get all SQL script files in the specified directory
sql_files = glob(os.path.join(script_directory, '*.sql'))

# Debugging: print found SQL files
print(f"Found SQL files: {sql_files}")

def execute_sql_script(server_config, sql_script):
    try:
        print(f"Connecting to server: {server_config['server']}, database: {server_config['database']}")
        
        # Establish the connection
        conn = pyodbc.connect(
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={server_config['server']};"
            f"DATABASE={server_config['database']};"
            f"UID={server_config['username']};"
            f"PWD={server_config['password']}"
        )
        
        # Debugging: Confirm connection
        print(f"Connected to {server_config['server']}")

        # Read SQL script and split by 'GO' commands
        with open(sql_script, 'r') as file:
            sql_queries = file.read().split('GO')

        # Execute each SQL batch
        cursor = conn.cursor()
        for query in sql_queries:
            query = query.strip()
            if query:  # Skip empty queries
                cursor.execute(query)
                cursor.commit()
        
        print(f"Deployment of {os.path.basename(sql_script)} to {server_config['database']} on {server_config['server']} completed successfully.")
        
    except Exception as e:
        print(f"Deployment of {os.path.basename(sql_script)} to {server_config['database']} on {server_config['server']} failed. Error: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

# Loop through each server and deploy each script
for server in servers:
    for sql_file in sql_files:
        print(f"Deploying {sql_file} to server {server['server']}")
        execute_sql_script(server, sql_file)
