import docker
import os

# Initialize Docker client
client = docker.from_env()

# Define the image to pull
image_name = "nginx:latest"

# Pull the image
print(f"Pulling image: {image_name}")
client.images.pull(image_name)

# Tag the image for ACR
acr_server = 'cregnedemo.azurecr.io'
acr_image_name = 'nginx'
acr_tag = 'latest'

acr_image_full_name = f"{acr_server}/{acr_image_name}:{acr_tag}"
print(f"Tagging image: {acr_image_full_name}")
client.images.get(image_name).tag(acr_image_full_name)

# Authenticate Docker client with ACR
acr_username = os.environ.get('ACR_USERNAME')
acr_password = os.environ.get('ACR_PASSWORD')
client.login(username=acr_username, password=acr_password, registry=acr_server)

# Push the tagged image to ACR
print(f"Pushing image to ACR: {acr_image_full_name}")
client.images.push(acr_image_full_name)

print("Image pushed to ACR successfully!")
