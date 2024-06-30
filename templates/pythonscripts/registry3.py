# working code 
# """
# Module for handling the registry operations and pushing Docker images to Azure Container Registry.
# """
# import subprocess
# import argparse

# def registry(acr_server,image_name,tag,login_command):
    


#     pull_command = f"docker pull {image_name}:{tag}"
#     subprocess.run(pull_command, shell=True, check=True)

#     tag_command = f"docker tag {image_name}:{tag} {acr_server}/{image_name}:{tag}"
#     subprocess.run(tag_command, shell=True, check=True)
   
#     subprocess.run(login_command, shell=True, check=True)

#     acr_login_command = f"az acr login --name {acr_server}"
#     subprocess.run(acr_login_command, shell=True, check=True)

#     push_command = f"docker push {acr_server}/{image_name}:{tag}"
#     subprocess.run(push_command, shell=True, check=True)

#     print("Image pushed to ACR successfully!")

# def main():
#     acr_server = 'cregnespendkey123.azurecr.io'
#     image_name = 'nginx'
#     tag = 'latest'  
#     login_command  = "az account set --subscription 187571e3-c50d-49ea-983f-41a86de0c2ec"
#     # login_command = f"az login --tenant 187571e3-c50d-49ea-983f-41a86de0c2ec"
#     registry(acr_server,image_name,tag,login_command)    

# if __name__ == "__main__":
#     main()



"""
Module for handling the registry operations and pushing Docker images to Azure Container Registry.
"""
import subprocess
import argparse

def registry(acr_server,image_name,tag,login_command):
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--acr_server", dest="acr_server", help="acr server",required=True)
    parser.add_argument("--login_command", dest="login_command", help="login command",required=True)
    args = parser.parse_args()


    pull_command = f"docker pull {image_name}:{tag}"
    subprocess.run(pull_command, shell=True, check=True)

    tag_command = f"docker tag {image_name}:{tag} {acr_server}/{image_name}:{tag}"
    subprocess.run(tag_command, shell=True, check=True)
   
    subprocess.run(login_command, shell=True, check=True)

    acr_login_command = f"az acr login --name {acr_server}"
    subprocess.run(acr_login_command, shell=True, check=True)

    push_command = f"docker push {acr_server}/{image_name}:{tag}"
    subprocess.run(push_command, shell=True, check=True)

    print("Image pushed to ACR successfully!")

def main():
    acr_server = 'cregnespendkey123.azurecr.io'
    image_name = 'nginx'
    tag = 'latest'  
    login_command  = "az account set --subscription 187571e3-c50d-49ea-983f-41a86de0c2ec"
    # login_command = f"az login --tenant 187571e3-c50d-49ea-983f-41a86de0c2ec"
    registry(acr_server,image_name,tag,login_command)    

if __name__ == "__main__":
    main()