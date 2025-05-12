# IoT Greengrass Terraform Project

Welcome to my project, I was just getting a grasp on how things work.

## What this project does
- Provisions an AWS IoT Thing and attaches a certificate using Terraform
- Registers a Greengrass component
- Deploys a Docker container to simulate local edge processing
- Publishes mock sensor data from a simulated IoT device using MQTT

## How to use
1. Navigate to the `terraform` directory ( `cd terraform` from the root of the project ) and run `terraform init` & `terraform apply`.
2. Save the certs from Terraform outputs into files used by the mock publisher:
    ```
    terraform output -raw certificate_pem > device.pem.crt
    terraform output -raw private_key > private.pem.key
    terraform output -raw public_key > public.pem.key

    curl https://www.amazontrust.com/repository/AmazonRootCA1.pem -o AmazonRootCA1.pem
    ```
3. Build and deploy the Docker component locally to simulate Greengrass:
    ```
    cd ../greengrass_component
    docker build -t my-local-temp-processor .

    aws greengrassv2 create-component-version \
    --inline-recipe fileb://../terraform/greengrass_component.json
    ```
4. Run the publisher script:
    ```
    IOT_ENDPOINT=$(terraform output -raw iot_endpoint) python ../simulate_device/publisher.py
    ```