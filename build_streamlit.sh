#!/usr/bin/env bash
set -euo pipefail
 
# Variables
APP_NAME="streamlit-ui"
IMAGE_NAME="streamlit-app:latest"
ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
APP_DIR="$ROOT_DIR/streamlit_app"
DEPLOY_DIR="$ROOT_DIR/k8s/ui-streamlit"
 
echo "📦 1) Cambiando a entorno Docker de Minikube"
eval $(minikube docker-env)
 
echo "🐳 2) Construyendo imagen Docker para $APP_NAME"
docker build -t "$IMAGE_NAME" "$APP_DIR"
 
echo "🚀 3) Aplicando Deployment y Service"
kubectl apply -f "$DEPLOY_DIR/streamlit-deployment.yml"
kubectl apply -f "$DEPLOY_DIR/streamlit-service.yml"
 
echo "⏳ 4) Esperando a que el deployment esté disponible..."
kubectl rollout status deployment/$APP_NAME -n mlops-proyecto3
 
echo "🌐 5) Accediendo vía NodePort (si estás en Minikube)..."
NODE_PORT=$(kubectl get svc streamlit-ui-service -n mlops-proyecto3 -o=jsonpath='{.spec.ports[0].nodePort}')
MINIKUBE_IP=$(minikube ip)
 
echo -e "\n✅ Streamlit está desplegado. Accede en tu navegador a:"
echo "👉 http://$MINIKUBE_IP:$NODE_PORT"