
import subprocess
import os 







def main():
    acr_server = 'cregnespendkey123.azurecr.io'
    image_name = 'nginx'
    tag = 'latest'

    pull_command = f"docker pull {image_name}:{tag}"
    subprocess.run(pull_command, shell=True, check=True)

    tag_command = f"docker tag {image_name}:{tag} {acr_server}/{image_name}:{tag}"
    subprocess.run(tag_command, shell=True, check=True)
    
    # Authenticate Docker client with ACR using managed identity
    login_command  = f" az account set --subscription 187571e3-c50d-49ea-983f-41a86de0c2ec"
    # login_command = f"az login --tenant 187571e3-c50d-49ea-983f-41a86de0c2ec"

    # login_command = f"az login"
    subprocess.run(login_command, shell=True, check=True)

    # Authenticate with ACR using managed identity
    acr_login_command = f"az acr login --name {acr_server}"
    subprocess.run(acr_login_command, shell=True, check=True)

    # Push the tagged image to ACR
    push_command = f"docker push {acr_server}/{image_name}:{tag}"
    subprocess.run(push_command, shell=True, check=True)

    print("Image pushed to ACR successfully!")


if __name__ == "__main__":
    main()