import os
import pyodbc
from glob import glob

# Configuration for Azure SQL Server connections
servers = [
    {
        'server':  'sqlsrv-ne-dev-spendkey1.database.windows.net',
        'database': 'sqldb-ne-dev-sk',
        'username': 'CloudSA697e03f6',
        'password': 'wpxfTCd?K3R+73U~CPWo@TNMBt3@%',
    },
    
]

# Directory containing the SQL scripts
script_directory = os.path.join(os.getcwd(), 'sql_scripts')

# Get all SQL script files in the specified directory
sql_files = glob(os.path.join(script_directory, '*.sql'))

def execute_sql_script(server_config, sql_script):
    try:
        # Establish the connection
        conn = pyodbc.connect(
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={server_config['server']};"
            f"DATABASE={server_config['database']};"
            f"UID={server_config['username']};"
            f"PWD={server_config['password']}"
        )
        
        # Read SQL script
        with open(sql_script, 'r') as file:
            sql_query = file.read()
        
        # Execute the SQL script
        cursor = conn.cursor()
        cursor.execute(sql_query)
        cursor.commit()
        
        print(f"Deployment of {os.path.basename(sql_script)} to {server_config['database']} on {server_config['server']} completed successfully.")
        
    except Exception as e:
        print(f"Deployment of {os.path.basename(sql_script)} to {server_config['database']} on {server_config['server']} failed. Error: {e}")
    finally:
        cursor.close()
        conn.close()

# Loop through each server and deploy each script
for server in servers:
    for sql_file in sql_files:
        execute_sql_script(server, sql_file)
