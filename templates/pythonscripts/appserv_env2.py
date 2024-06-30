import subprocess
import json
import argparse
import os
from azure.mgmt.web import WebSiteManagementClient
from azure.identity import DefaultAzureCredential
from azure.mgmt.web.models import SiteConfig, NameValuePair

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
    # parser.add_argument("--acr_server", dest="acr_server", help="acr server",required=True)
    parser.add_argument("--login_command", dest="login_command", help="login command",nargs='+',required=True)
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

    print("Registry username:", registry_username)
    print("Registry login server:", registry_login_server)
    print("Registry password:", registry_password)

    app_settings = [
        NameValuePair(name="DOCKER_REGISTRY_SERVER_USERNAME", value=registry_username),
        NameValuePair(name="DOCKER_REGISTRY_SERVER_PASSWORD", value=registry_password),
        NameValuePair(name="DOCKER_REGISTRY_SERVER_URL", value=registry_login_server),
        # NameValuePair(name="loginServer", value=registry_login_server)  # Include loginServer in app settings
    ]
    
    credential = DefaultAzureCredential()

    web_app_name = f"app-angular-{args.urlname}"
    web_client = WebSiteManagementClient(credential, args.subscriptionId)   
    web_app = web_client.web_apps.get(args.resourceGroupName, web_app_name)

    # Initialize app_settings as an empty list if it's None
    app_settings_existing = web_app.site_config.app_settings or []
    app_settings_existing.extend(app_settings)

    site_config = SiteConfig(app_settings=app_settings_existing)
    web_app.site_config = site_config

    web_client.web_apps.begin_create_or_update(args.resourceGroupName, web_app_name, web_app)
    print("Output values have been passed to the Azure App Service successfully.")

    
def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--urlname", dest="urlname", help="URL name for ACR", required=True)
    parser.add_argument("--login_command", dest="login_command", help="login command", nargs='+', required=True)
    parser.add_argument("--subscriptionId", dest="subscriptionId", help="Azure subscription ID", required=True)
    parser.add_argument("--resourceGroupName", dest="resourceGroupName", help="Azure resourceGroupName", required=True)
    args = parser.parse_args()
    update_env(args)
    
    # update_env()
    # acr_credentials_command = "az acr credential show --name cregdos --output json"
    # login_command = f"az account set --subscription 187571e3-c50d-49ea-983f-41a86de0c2ec"
    # login_command = "az login --tenant 862921fd-f4cb-4a0f-86e9-c450994eb3f9"
    # subscription_id = '187571e3-c50d-49ea-983f-41a86de0c2ec'
    # resource_group_name = 'myRG'
    # web_app_name = 'app-angular-dos'
    
    
if __name__ == "__main__":
    main()
    
 


