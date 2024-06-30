"""
Module for handling the registry operations and pushing Docker images to Azure Container Registry.
"""
import subprocess
import argparse


def registry():
      
    parser = argparse.ArgumentParser()
    parser.add_argument("--acr_server", dest="acr_server", help="acr server",required=True)
    parser.add_argument("--login_command", dest="login_command", help="login command",nargs='+',required=True)
    parser.add_argument("--subscriptionId", dest="subscriptionId", help="Azure subscription ID", required=False)
    args = parser.parse_args()
    
    image_name = 'nginx'
    tag = 'latest' 
     
    pull_command = f"docker pull {image_name}:{tag}"
    subprocess.run(pull_command, shell=True, check=True)

    tag_command = f"docker tag {image_name}:{tag} {args.acr_server}/{image_name}:{tag}"
    subprocess.run(tag_command, shell=True, check=True)
    
    subprocess.run(args.login_command, shell=True, check=True)

    acr_login_command = f"az acr login --name {args.acr_server}"
    subprocess.run(acr_login_command, shell=True, check=True)

    push_command = f"docker push {args.acr_server}/{image_name}:{tag}"
    subprocess.run(push_command, shell=True, check=True)

    print("Image pushed to ACR successfully!")

def main():
    registry()    

if __name__ == "__main__":
    main()