import subprocess
import json
import argparse
import os

def execute_az_cli_command(command):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        print(f"Error executing command: {command}")
        print(result.stderr)
        return None
    else:
        try:
            return json.loads(result.stdout.strip())
        except json.JSONDecodeError as e: 
            print(f"Error decoding JSON output: {e}")
            return None

def update_env(args):

    login_command_str = ' '.join(args.login_command)
    os.system(login_command_str)

    parser = argparse.ArgumentParser()
    parser.add_argument("--urlname", dest="urlname", help="URL name for ACR", required=True)
    parser.add_argument("--login_command", dest="login_command", help="login command", nargs='+', required=True)
    parser.add_argument("--subscriptionId", dest="subscriptionId", help="Azure subscription ID", required=False)    
    parser.add_argument("--resourceGroupName", dest="resourceGroupName", help="Azure resourceGroupName", required=False)
    args = parser.parse_args()
    
    acr_credentials_command = f"az acr credential show --name creg{args.urlname} --output json"
    acr_credentials_output = execute_az_cli_command(acr_credentials_command)
    print("ACR credentials output:", acr_credentials_output)

    if not acr_credentials_output:
        print("Error parsing or extracting output.")
        return

    registry_username = acr_credentials_output.get("username")
    registry_password = acr_credentials_output["passwords"][0]["value"]
    registry_login_server = f"https://{registry_username}.azurecr.io"
    registry_website_port = f"51011"
    registry_website_sync = f"true"
    registry_retention_day = f"3"    

    print("Registry username:", registry_username)
    print("Registry login server:", registry_login_server)
    print("Registry password:", registry_password)
    print("Registry website port:", registry_website_port)
    print("Registry websitesync:", registry_website_sync)
    print("Registry retention day:", registry_retention_day)
    
    # Construct app settings
    app_settings = [
        {"name": "DOCKER_REGISTRY_SERVER_USERNAME", "value": registry_username},
        {"name": "DOCKER_REGISTRY_SERVER_PASSWORD", "value": registry_password},
        {"name": "DOCKER_REGISTRY_SERVER_URL", "value": registry_login_server},
        {"name": "WEBSITES_PORT", "value": registry_website_port},
        {"name": "WEBSITE_ENABLE_SYNC_UPDATE_SITE", "value": registry_website_sync},
        {"name": "WEBSITE_HTTPLOGGING_RETENTION_DAYS", "value": registry_retention_day}        
        
    ]

    # Update Azure App Service configuration
    update_command = f"az webapp config appsettings set --name app-microservice-{args.urlname} --resource-group {args.resourceGroupName} --settings"
    for setting in app_settings:
        update_command += f" {setting['name']}={setting['value']}"

    result = execute_az_cli_command(update_command)
    if result:
        print("Output values have been passed to the Azure App Service successfully.")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--urlname", dest="urlname", help="URL name for ACR", required=True)
    parser.add_argument("--login_command", dest="login_command", help="login command", nargs='+', required=True)
    parser.add_argument("--subscriptionId", dest="subscriptionId", help="Azure subscription ID", required=True)
    parser.add_argument("--resourceGroupName", dest="resourceGroupName", help="Azure resourceGroupName", required=True)
    args = parser.parse_args()
    update_env(args)

if __name__ == "__main__":
    main()
