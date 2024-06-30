import os
import pyodbc
from glob import glob
import argparse

def get_sql_files(script_directory):
    """Get all SQL script files in the specified directory."""
    sql_files = glob(os.path.join(script_directory, '*.sql'))
    if not sql_files:
        print(f"No SQL files found in directory: {script_directory}")
    else:
        print(f"Found SQL files: {sql_files}")  # Debugging: print found SQL files
    return sql_files

def execute_sql_script(server_config, database, sql_script):
    """Execute a SQL script on a specified server configuration and database."""
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
        
        print(f"Connected to {server_config['server']}")  # Debugging: Confirm connection

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
        
        print(f"Deployment of {os.path.basename(sql_script)} to {database} on {server_config['server']} completed successfully.")
        
    except Exception as e:
        print(f"Deployment of {os.path.basename(sql_script)} to {database} on {server_config['server']} failed. Error: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

def multi_script(server_config, script_directory):
    """Deploy SQL scripts to multiple databases on a single server."""
    sql_files = get_sql_files(script_directory)
    
    # Loop through each database and deploy each script
    for database in server_config['databases']:
        for sql_file in sql_files:
            print(f"Deploying {sql_file} to server {server_config['server']} and database {database}")
            execute_sql_script(server_config, database, sql_file)

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Deploy SQL scripts to multiple databases on a single server.')
    parser.add_argument('--FolderName', type=str, required=True, help='Name of the directory containing the SQL scripts')
    return parser.parse_args()

def main():
    args = parse_arguments()
    script_directory = os.path.join(os.getcwd(), args.FolderName)
    
    server_config = {
        'server': 'sqlsrv-ne-dev-spendkey1.database.windows.net',
        'databases': ['sqldb-ne-reckittdev-spendkey', 'sqldb-ne-test2-spendkey'],  # List of databases within the same SQL Server
        'username': 'CloudSA697e03f6',
        'password': 'wpxfTCd?K3R+73U~CPWo@TNMBt3@%',
    }
    
    multi_script(server_config, script_directory)

if __name__ == "__main__":
    main()




# import os
# import pyodbc
# from glob import glob
# import argparse

# def get_sql_files(script_directory):
#     """Get all SQL script files in the specified directory."""
#     sql_files = glob(os.path.join(script_directory, '*.sql'))
#     print(f"Found SQL files: {sql_files}")  # Debugging: print found SQL files
#     return sql_files

# def execute_sql_script(server_config, database, sql_script):
#     """Execute a SQL script on a specified server configuration and database."""
#     try:
#         print(f"Connecting to server: {server_config['server']}, database: {database}")
        
#         # Establish the connection
#         conn = pyodbc.connect(
#             f"DRIVER={{ODBC Driver 17 for SQL Server}};"
#             f"SERVER={server_config['server']};"
#             f"DATABASE={database};"
#             f"UID={server_config['username']};"
#             f"PWD={server_config['password']}"
#         )
        
#         print(f"Connected to {server_config['server']}")  # Debugging: Confirm connection

#         # Read SQL script and split by 'GO' commands
#         with open(sql_script, 'r') as file:
#             sql_queries = file.read().split('GO')

#         # Execute each SQL batch
#         cursor = conn.cursor()
#         for query in sql_queries:
#             query = query.strip()
#             if query:  # Skip empty queries
#                 cursor.execute(query)
#                 cursor.commit()
        
#         print(f"Deployment of {os.path.basename(sql_script)} to {database} on {server_config['server']} completed successfully.")
        
#     except Exception as e:
#         print(f"Deployment of {os.path.basename(sql_script)} to {database} on {server_config['server']} failed. Error: {e}")
#     finally:
#         if 'cursor' in locals():
#             cursor.close()
#         if 'conn' in locals():
#             conn.close()

# def multi_script(server_config, script_directory):
#     """Deploy SQL scripts to multiple databases on a single server."""
#     sql_files = get_sql_files(script_directory)

#     # Loop through each database and deploy each script
#     for database in server_config['databases']:
#         for sql_file in sql_files:
#             print(f"Deploying {sql_file} to server {server_config['server']} and database {database}")
#             execute_sql_script(server_config, database, sql_file)

# def parse_arguments():
#     """Parse command line arguments."""
#     parser = argparse.ArgumentParser(description='Deploy SQL scripts to multiple databases on a single server.')
#     parser.add_argument('--FolderName', type=str, required=True, help='Name of the directory containing the SQL scripts')
#     return parser.parse_args()

# def main():
#     args = parse_arguments()
#     script_directory = os.path.join(os.getcwd(), args.FolderName)
    
#     server_config = {
#         'server': 'sqlsrv-ne-dev-spendkey1.database.windows.net',
#         'databases': ['sqldb-ne-reckittdev-spendkey', 'sqldb-ne-test2-spendkey'],  # List of databases within the same SQL Server
#         'username': 'CloudSA697e03f6',
#         'password': 'wpxfTCd?K3R+73U~CPWo@TNMBt3@%',
#     },
    
#     multi_script(server_config, script_directory)

# if __name__ == "__main__":
#     main()
