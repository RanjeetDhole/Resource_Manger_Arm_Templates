import os
import pyodbc
from glob import glob
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--FolderName", dest="FolderName", help="FolderName", required=True)
args = parser.parse_args()

server_config = {
        'server': 'sqlsrv-ne-dev-spendkey1.database.windows.net',
        'databases': ['sqldb-ne-dev-sk', 'sqldb-ne-dentsu-spendkey','sqldb-ne-mundipharmadev-spendkey','sqldb-ne-juliusbaer-spendkey'],  # List of databases within the same SQL Server change database names or addded 
        'username': 'CloudSA697e03f6',
        'password': 'wpxfTCd?K3R+73U~CPWo@TNMBt3@%',
    }

# Directory containing the SQL scripts
script_directory = os.path.join(os.getcwd(),'SpendkeyDevops/devops/scripts/pythonscripts',args.FolderName)



# Debugging: Print the full script directory path
print(f"Looking for SQL files in directory: {script_directory}")

# Check if the directory exists
if not os.path.isdir(script_directory):
    print(f"Directory does not exist: {script_directory}")
else:
    # Debugging: List the contents of the directory
    directory_contents = os.listdir(script_directory)
    print(f"Contents of {script_directory}: {directory_contents}")




# Get all SQL script files in the specified directory
sql_files = glob(os.path.join(script_directory, '*.sql'))
print(f"Found SQL files: {sql_files}")

# Connect and execute SQL scripts
for database in server_config['databases']:
    for sql_file in sql_files:
        try:
            print(f"Connecting to server: {server_config['server']}, database: {database}")
            
            # Establish the connection
            conn = pyodbc.connect(
                f"DRIVER={{ODBC Driver 17 for SQL Server}};"
                f"SERVER={server_config['server']};"
                f"DATABASE={database};"
                f"UID={server_config['username']};"
                f"PWD={server_config['password']}"
            )
            
            print(f"Connected to {server_config['server']}")

            # Read SQL script and split by 'GO' commands
            with open(sql_file, 'r') as file:
                sql_queries = file.read().split('GO')

            # Execute each SQL batch
            cursor = conn.cursor()
            for query in sql_queries:
                query = query.strip()
                if query:  # Skip empty queries
                    cursor.execute(query)
                    cursor.commit()
            
            print(f"Deployment of {os.path.basename(sql_file)} to {database} on {server_config['server']} completed successfully.")
            
        except Exception as e:
            print(f"Deployment of {os.path.basename(sql_file)} to {database} on {server_config['server']} failed. Error: {e}")
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conn' in locals():
                conn.close()
