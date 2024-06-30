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
#             print(f"Error decoding JOSN output: {e}")
#             return None
#         # return result.stdout.strip()

# az_login_command = "az login"
# os.system(az_login_command)


# # acr_credentials_command = "az acr credential show --name cregnespendkey123 --query '[username,passwords[0].value]' --output json"
# acr_credentials_command = "az acr credential show --name cregnespendkey123 --output json"
# acr_credentials_output = execute_az_cli_command(acr_credentials_command)
# print("ACR credentials output:", acr_credentials_output)

# try:
#     acr_credentials_data = json.loads(acr_credentials_output)
#     registry_username = acr_credentials_data[0]["username"]
#     registry_password = acr_credentials_data[0]["passwords"][0]["value"]
#     print("Registry username:", registry_username)
#     print("Registry password:", registry_password)
# except (ValueError, KeyError, IndexError) as e:
#     print("Error parsing or extracting output:", e)
#     registry_username = None
#     registry_password = None
    
# output_values = {
#     "registryUsername": registry_username,
#     "registryPassword": registry_password
# }

# credential = DefaultAzureCredential()

# subscription_id = '187571e3-c50d-49ea-983f-41a86de0c2ec'
# resource_group_name = 'myRG'
# web_app_name = 'app-ne-spendkey-angular'
# web_client = WebSiteManagementClient(credential, subscription_id)

# web_app = web_client.web_apps.get(resource_group_name, web_app_name)

# app_settings = web_app.site_config.app_settings
# for key, value in output_values.items():
#     app_settings.append(NameValuePair(key, value))


# site_config = SiteConfig(app_settings=app_settings)
# web_app.site_config = site_config
# web_client.web_apps.create_or_update(resource_group_name, web_app_name, web_app)

# print("Output values have been passed to the Azure App Service successfully.")

# ///////


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

# az_login_command = "az login"
# os.system(az_login_command)

# acr_credentials_command = "az acr credential show --name cregnespendkey123 --output json"
# acr_credentials_output = execute_az_cli_command(acr_credentials_command)
# print("ACR credentials output:", acr_credentials_output)

# try:
#     registry_login_server =  acr_credentials_output["loginServer"]
#     registry_username = acr_credentials_output["username"]
#     registry_password = acr_credentials_output["passwords"][0]["value"]
#     print("Registry username:", registry_username)
#     print("loginServer: ", registry_login_server)
#     print("Registry password:", registry_password)
# except (ValueError, KeyError, IndexError) as e:
#     print("Error parsing or extracting output:", e)
#     registry_login_server = None
#     registry_username = None
#     registry_password = None
    
# output_values = {
#     "registry_login_server": registry_login_server,
#     "registryUsername": registry_username,
#     "registryPassword": registry_password
# }

# credential = DefaultAzureCredential()

# subscription_id = '187571e3-c50d-49ea-983f-41a86de0c2ec'
# resource_group_name = 'myRG'
# web_app_name = 'app-ne-spendkey-angular'
# web_client = WebSiteManagementClient(credential, subscription_id)

# web_app = web_client.web_apps.get(resource_group_name, web_app_name)

# app_settings = web_app.site_config.app_settings
# for key, value in output_values.items():
#     app_settings.append(NameValuePair(key, value))

# site_config = SiteConfig(app_settings=app_settings)
# web_app.site_config = site_config
# web_client.web_apps.create_or_update(resource_group_name, web_app_name, web_app)

# print("Output values have been passed to the Azure App Service successfully.")


# --///////

import os
import subprocess
import json
from azure.identity import DefaultAzureCredential
from azure.mgmt.web import WebSiteManagementClient
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

az_login_command = "az login"
os.system(az_login_command)

acr_credentials_command = "az acr credential show --name cregnespendkey123 --output json"
acr_credentials_output = execute_az_cli_command(acr_credentials_command)
print("ACR credentials output:", acr_credentials_output)

registry_username = None
registry_login_server = None
registry_password = None

if acr_credentials_output:
    registry_username = acr_credentials_output.get("username")
    registry_password = acr_credentials_output["passwords"][0]["value"]
    registry_login_server = acr_credentials_output.get("loginServer")

    print("Registry username:", registry_username)
    print("Registry login server:", registry_login_server)
    print("Registry password:", registry_password)
else:
    print("Error parsing or extracting output.")

output_values = {
    "registry_login_server": registry_login_server,
    "registryUsername": registry_username,
    "registryPassword": registry_password
}

credential = DefaultAzureCredential()

subscription_id = '187571e3-c50d-49ea-983f-41a86de0c2ec'
resource_group_name = 'myRG'
web_app_name = 'app-ne-spendkey-angular'
web_client = WebSiteManagementClient(credential, subscription_id)

web_app = web_client.web_apps.get(resource_group_name, web_app_name)

# Initialize app_settings as an empty list if it's None
app_settings = web_app.site_config.app_settings or []

for key, value in output_values.items():
    if value is not None:
        app_settings.append(NameValuePair(name= key, value= value))

site_config = SiteConfig(app_settings=app_settings)
web_app.site_config = site_config
# web_client.web_apps.create_or_update(resource_group_name, web_app_name, web_app)
web_client.web_apps.begin_create_or_update(resource_group_name, web_app_name, web_app)

print("Output values have been passed to the Azure App Service successfully.")


