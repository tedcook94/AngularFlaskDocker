#!/bin/bash

# Get directory of this script
this_dir=${0%/*}
this_dir=${this_dir%\\*}

# Build and push database image
cd "${this_dir}"
cd ../../database
docker build -f ua.Dockerfile -t tedcook94/angularflask_database:ua .
docker push tedcook94/angularflask_database:ua

# Build and push server image
cd ../server
docker build -f ua.Dockerfile -t tedcook94/angularflask_server:ua .
docker push tedcook94/angularflask_server:ua

# Build and push client image
cd ../client
docker build -f ua.Dockerfile -t tedcook94/angularflask_client:ua .
docker push tedcook94/angularflask_client:ua

# Change back to ua directory
cd "${this_dir}"

# Install Kubernetes metrics server
kubectl apply -f ./metrics-server.yaml

# Apply ConfigMap
kubectl apply -f ./ua-env-configmap.yaml

# Apply database PersistentVolumeClaim, Deployment and Service
kubectl apply -f ./database-data-pvc.yaml
kubectl apply -f ./database-deployment.yaml
kubectl apply -f ./database-service.yaml

# Apply server Deployment, Service and HorizontalPodAutoscaler
kubectl apply -f ./server-deployment.yaml
kubectl apply -f ./server-service.yaml
kubectl apply -f ./server-hpa.yaml

# Apply client Deployment, Service and HorizontalPodAutoscaler
kubectl apply -f ./client-deployment.yaml
kubectl apply -f ./client-service.yaml
kubectl apply -f ./client-hpa.yaml

# Apply Ingress
kubectl apply -f ./aws-ingress.yaml

# Trigger a rolling update in case pods already exist
kubectl rollout restart deployment database
kubectl rollout restart deployment server
kubectl rollout restart deployment client

printf '\n'
read -n 1 -s -r -p "Press any key to continue..."