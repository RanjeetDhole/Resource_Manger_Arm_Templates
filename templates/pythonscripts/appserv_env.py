# working -----------------------\
# import os
# import subprocess
# import json
# from azure.identity import DefaultAzureCredential
# from azure.mgmt.web import WebSiteManagementClient
# from azure.mgmt.web.models import SiteConfig, NameValuePair

# def execute_az_cli_command(command):
#     result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#     if result.returncode != 0:
#         print(f"Error executing command: {command}")
#         print(result.stderr)
#         return None
#     else:
#         try:
#             return json.loads(result.stdout.strip())
#         except json.JSONDecodeError as e: 
#             print(f"Error decoding JSON output: {e}")
#             return None

# def update_env(login_command,acr_credentials_command,subscription_id,resource_group_name,web_app_name):
#     login_command = "az login"
#     os.system(login_command)

#     acr_credentials_output = execute_az_cli_command(acr_credentials_command)
#     print("ACR credentials output:", acr_credentials_output)

#     registry_username = None
#     registry_login_server = None
#     registry_password = None

#     if acr_credentials_output:
#         registry_username = acr_credentials_output.get("username")
#         registry_password = acr_credentials_output["passwords"][0]["value"]
#         registry_login_server = acr_credentials_output.get("loginServer")

#         print("Registry username:", registry_username)
#         print("Registry login server:", registry_login_server)
#         print("Registry password:", registry_password)
#     else:
#         print("Error parsing or extracting output.")

#     output_values = {
#         "registry_login_server": registry_login_server,
#         "registryUsername": registry_username,
#         "registryPassword": registry_password,
#         "loginServer": registry_login_server
#     }

#     credential = DefaultAzureCredential()

#     web_client = WebSiteManagementClient(credential, subscription_id)
#     web_app = web_client.web_apps.get(resource_group_name, web_app_name)

#     # Initialize app_settings as an empty list if it's None
#     app_settings = web_app.site_config.app_settings or []

#     for key, value in output_values.items():
#         if value is not None:
#             app_settings.append(NameValuePair(name= key, value= value))
            
#     site_config = SiteConfig(app_settings=app_settings)
#     web_app.site_config = site_config

#     web_client.web_apps.begin_create_or_update(resource_group_name, web_app_name, web_app)
#     print("Output values have been passed to the Azure App Service successfully.")

    
# def main():
#     acr_credentials_command = "az acr credential show --name cregnespendkey123 --output json"
#     login_command = "az account set --subscription 187571e3-c50d-49ea-983f-41a86de0c2ec"
#     subscription_id = '187571e3-c50d-49ea-983f-41a86de0c2ec'
#     resource_group_name = 'myRG'
#     web_app_name = 'app-ne-spendkey-angular'
#     update_env(login_command,acr_credentials_command,subscription_id,resource_group_name,web_app_name)    
    
# if __name__ == "__main__":
#     main()   


# working second 
# import os
# import subprocess
# import json
# from azure.identity import DefaultAzureCredential
# from azure.mgmt.web import WebSiteManagementClient
# from azure.mgmt.web.models import SiteConfig, NameValuePair

# def execute_az_cli_command(command):
#     result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#     if result.returncode != 0:
#         print(f"Error executing command: {command}")
#         print(result.stderr)
#         return None
#     else:
#         try:
#             return json.loads(result.stdout.strip())
#         except json.JSONDecodeError as e: 
#             print(f"Error decoding JSON output: {e}")
#             return None

# def update_env(login_command,acr_credentials_command,subscription_id,resource_group_name,web_app_name):
#     login_command = "az login"
#     os.system(login_command)

#     acr_credentials_output = execute_az_cli_command(acr_credentials_command)
#     print("ACR credentials output:", acr_credentials_output)

#     registry_username = None
#     registry_login_server = None
#     registry_password = None

#     if acr_credentials_output:
#         registry_username = acr_credentials_output.get("username")
#         registry_login_server = acr_credentials_output.get("loginServer")
#         registry_password = acr_credentials_output["passwords"][0]["value"]
        

#         print("Registry username:", registry_username)
#         print("Registry login server:", registry_login_server)
#         print("Registry password:", registry_password)
#     else:
#         print("Error parsing or extracting output.")
        
#     app_settings = []

#     if registry_username:
#         app_settings.append(NameValuePair(name="registryUsername", value=registry_username))
#     if registry_login_server:
#         app_settings.append(NameValuePair(name="registry_login_server", value=registry_login_server))        
#     if registry_password:
#         app_settings.append(NameValuePair(name="registryPassword", value=registry_password))

        
#     output_values = {
#         "registry_login_server": registry_login_server,
#         "registryUsername": registry_username,
#         "registryPassword": registry_password,
#         "loginServer": registry_login_server
#     }

#     credential = DefaultAzureCredential()

#     web_client = WebSiteManagementClient(credential, subscription_id)
#     web_app = web_client.web_apps.get(resource_group_name, web_app_name)

#     # Initialize app_settings as an empty list if it's None
#     app_settings = web_app.site_config.app_settings or []

#     for key, value in output_values.items():
#         if value is not None:
#             app_settings.append(NameValuePair(name= key, value= value))
            
#     site_config = SiteConfig(app_settings=app_settings)
#     web_app.site_config = site_config

#     web_client.web_apps.begin_create_or_update(resource_group_name, web_app_name, web_app)
#     print("Output values have been passed to the Azure App Service successfully.")

    
# def main():
#     acr_credentials_command = "az acr credential show --name cregnespendkey123 --output json"
#     login_command = "az account set --subscription 187571e3-c50d-49ea-983f-41a86de0c2ec"
#     subscription_id = '187571e3-c50d-49ea-983f-41a86de0c2ec'
#     resource_group_name = 'myRG'
#     web_app_name = 'app-ne-spendkey-angular'
#     update_env(login_command,acr_credentials_command,subscription_id,resource_group_name,web_app_name)    
    
# if __name__ == "__main__":
#     main()   


# working third------------------/

# import os
# import subprocess
# import json
# from azure.identity import DefaultAzureCredential
# from azure.mgmt.web import WebSiteManagementClient
# from azure.mgmt.web.models import SiteConfig, NameValuePair

# def execute_az_cli_command(command):
#     result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#     if result.returncode != 0:
#         print(f"Error executing command: {command}")
#         print(result.stderr)
#         return None
#     else:
#         try:
#             return json.loads(result.stdout.strip())
#         except json.JSONDecodeError as e: 
#             print(f"Error decoding JSON output: {e}")
#             return None

# def update_env(login_command, acr_credentials_command, subscription_id, resource_group_name, web_app_name):
#     login_command = "az login"
#     os.system(login_command)

#     acr_credentials_output = execute_az_cli_command(acr_credentials_command)
#     print("ACR credentials output:", acr_credentials_output)

#     if not acr_credentials_output:
#         print("Error parsing or extracting output.")
#         return

#     registry_username = acr_credentials_output.get("username")
#     registry_password = acr_credentials_output["passwords"][0]["value"]
#     registry_login_server = acr_credentials_output.get("loginServer")

#     print("Registry username:", registry_username)
#     print("Registry login server:", registry_login_server)
#     print("Registry password:", registry_password)

#     app_settings = [
#         NameValuePair(name="registryUsername", value=registry_username),
#         NameValuePair(name="registryPassword", value=registry_password),
#         NameValuePair(name="registry_login_server", value=registry_login_server),
#         NameValuePair(name="loginServer", value=registry_login_server)  # Include loginServer in app settings
#     ]

#     credential = DefaultAzureCredential()

#     web_client = WebSiteManagementClient(credential, subscription_id)
#     web_app = web_client.web_apps.get(resource_group_name, web_app_name)

#     # Initialize app_settings as an empty list if it's None
#     app_settings_existing = web_app.site_config.app_settings or []
#     app_settings_existing.extend(app_settings)

#     site_config = SiteConfig(app_settings=app_settings_existing)
#     web_app.site_config = site_config

#     web_client.web_apps.begin_create_or_update(resource_group_name, web_app_name, web_app)
#     print("Output values have been passed to the Azure App Service successfully.")


    
# def main():
#     acr_credentials_command = "az acr credential show --name cregnespendkey123 --output json"
#     login_command = "az account set --subscription 187571e3-c50d-49ea-983f-41a86de0c2ec"
#     subscription_id = '187571e3-c50d-49ea-983f-41a86de0c2ec'
#     resource_group_name = 'myRG'
#     web_app_name = 'app-ne-spendkey-angular'
#     update_env(login_command,acr_credentials_command,subscription_id,resource_group_name,web_app_name)    
    
# if __name__ == "__main__":
#     main()   











# -----working code 

import os
import subprocess
import json
from azure.identity import DefaultAzureCredential
from azure.mgmt.web import WebSiteManagementClient
from azure.mgmt.web.models import SiteConfig, NameValuePair
import argparse

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

def update_env(login_command, acr_credentials_command, subscription_id, resource_group_name, web_app_name):
    # login_command = "az login"
    # os.system(login_command)
    
   
    # os.system("az login --tenant 862921fd-f4cb-4a0f-86e9-c450994eb3f9")
    # os.system(f"az login --tenant 862921fd-f4cb-4a0f-86e9-c450994eb3f9 --user ranjeet@spendkey.co.uk --password India@7726")
    os.system(login_command)
    # os.system(f"az login --user ranjeet@spendkey.co.uk --password India@7726")


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

    web_client = WebSiteManagementClient(credential, subscription_id)   
    web_app = web_client.web_apps.get(resource_group_name, web_app_name)

    # Initialize app_settings as an empty list if it's None
    app_settings_existing = web_app.site_config.app_settings or []
    app_settings_existing.extend(app_settings)

    site_config = SiteConfig(app_settings=app_settings_existing)
    web_app.site_config = site_config

    web_client.web_apps.begin_create_or_update(resource_group_name, web_app_name, web_app)
    print("Output values have been passed to the Azure App Service successfully.")


    
def main():
    acr_credentials_command = "az acr credential show --name cregdos --output json"
    login_command = f"az account set --subscription 187571e3-c50d-49ea-983f-41a86de0c2ec"
    # login_command = "az login --tenant 862921fd-f4cb-4a0f-86e9-c450994eb3f9"
    subscription_id = '187571e3-c50d-49ea-983f-41a86de0c2ec'
    resource_group_name = 'myRG'
    web_app_name = 'app-angular-dos'
    update_env(login_command,acr_credentials_command,subscription_id,resource_group_name,web_app_name)    
    
if __name__ == "__main__":
    main()
    
    
# az login --tenant 862921fd-f4cb-4a0f-86e9-c450994eb3f9 --subscription 187571e3-c50d-49ea-983f-41a86de0c2ec --user ranjeet@spendkey.co.uk --password India@7726


