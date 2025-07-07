# Estructura del proyecto y pasos de ejecucion

## Arbol del proyecto

```
MIgra-Orque-Final/
├── .github/
│   └── workflows/
│       └── deploy.yml
├── docker-compose.yml
├── initdb/
│   └── init.sql
├── kubernetes/
│   ├── configmap.yaml
│   ├── deployments.yaml
│   ├── ingress.yaml
│   ├── network-policy.yaml
│   ├── secret.yaml
│   └── statefulset.yaml
├── src/
│   ├── legacy-app/
│   │   ├── .dockerignore
│   │   ├── Dockerfile
│   │   ├── app.py
│   │   └── requirements.txt
│   └── microservice/
│       ├── .dockerignore
│       ├── Dockerfile
│       ├── app.py
│       └── requirements.txt
└── EJECUCION.md
└── README.md
```

## Pasos de ejecucion

### 1. Desarrollo local con docker compose

```bash
# construir y levantar servicios
docker-compose up --build

# verificar servicios
curl http://localhost:5000/health
curl http://localhost:8000/health
curl http://localhost:5000/api/data
```

### 2. Despliegue en kubernetes

```bash
# aplicar manifiestos en orden
kubectl apply -f kubernetes/secret.yaml
kubectl apply -f kubernetes/configmap.yaml
kubectl apply -f kubernetes/statefulset.yaml
kubectl apply -f kubernetes/deployments.yaml
kubectl apply -f kubernetes/network-policy.yaml
kubectl apply -f kubernetes/ingress.yaml

# se verifica despliegue
kubectl get pods
kubectl get services
kubectl get ingress
```

### 3. Acceso a las aplicaciones

```bash
# obtener ip de minikube
minikube ip

# acceder a aplicaciones
curl http://<minikube-ip>/app/health
curl http://<minikube-ip>/api/v2/health
```


