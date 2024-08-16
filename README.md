# Hello-World Flask Web Server

This is a simple Flask-based web server that alternates between displaying "Hello" and "World" each time it is accessed. It can be easily deployed locally using Docker or on a Kubernetes cluster.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running Locally](#running-locally)
- [Deploying to Kubernetes](#deploying-to-kubernetes)
- [Usage](#usage)
- [Cleanup](#cleanup)

## Prerequisites

- Docker installed on your machine.
- Minikube installed (You can use any other cloud-based Kubernetes cluster).
- kubectl configured to interact with your Kubernetes cluster.
- A Docker Hub account (or any other container registry).

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/judeoyovbaire/tech-assignment-dta.git
    cd tech-assignment-dta
    ```

2. Build the Docker image:

    ```bash
    docker build -t <your-dockerhub-username>/hello-world:latest .
    ```

3. Push the Docker image to Docker Hub:

    ```bash
    docker push <your-dockerhub-username>/hello-world:latest
    ```

## Running Locally

To run the application locally using Docker:

1. Build the Docker image:

    ```bash
    docker build -t hello-world .
    ```

2. Run the Docker container:

    ```bash
    docker run -p 5500:5500 hello-world
    ```

3. Access the application at [http://localhost:5000](http://localhost:5000).

## Deploying to Kubernetes

To deploy the application to a Kubernetes cluster:

1. Ensure your Docker image is pushed to Docker Hub (or any other accessible container registry).

2. Update the `deployment.yaml` file if necessary, particularly the image name:

    ```yaml
    containers:
    - name: hello-world
      image: <your-dockerhub-username>/hello-world:latest
    ```

3. Apply the Kubernetes configuration:

    ```bash
    kubectl apply -f deployment.yaml
    ```

4. To find the external IP address of the service, run:

    ```bash
    kubectl get services
    ```

5. Access the application service via the Minikube service, run:

    ```bash
    minikube service <service-name>
    ```
   OR
    ```bash
    minikube service <service-name> --url
    ```

## Usage

- The first time you access the server, it will display "Hello".
- The next time, it will display "World".
- It alternates between "Hello" and "World" with each access.

## Cleanup

### Local Cleanup

To stop the Docker container running locally:

```bash
docker ps
docker stop <container_id>
