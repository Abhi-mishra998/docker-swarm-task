# ------------------------------
# 1. Docker Build & Run Backend
# ------------------------------
docker build -t flask-backend:latest .
docker run -p 5000:5000 flask-backend:latest

# ------------------------------
# 2. Docker Compose (Local Development)
# ------------------------------
docker-compose up -d
docker-compose down
docker ps
docker-compose logs -f

# ------------------------------
# 3. Docker Swarm Setup
# ------------------------------
docker swarm init
docker swarm leave --force
docker stack deploy -c stack.yml myapp
docker stack services myapp
docker service ps myapp_backend
docker service update --image abhishek8056/flask-backend:vX myapp_backend
docker stack rm myapp

# ------------------------------
# 4. Docker Image Management
# ------------------------------
docker image ls
docker tag flask-backend:latest abhishek8056/flask-backend:v2
docker push abhishek8056/flask-backend:v2
docker rmi IMAGE_ID

# ------------------------------
# 5. Testing / Verification
# ------------------------------
curl http://localhost:5000/api
curl http://localhost:8090/api
curl http://localhost:8090/

# ------------------------------
# 6. Container Management
# ------------------------------
docker ps
docker stop CONTAINER_ID
docker rm CONTAINER_ID
