
Scenario
You are a DevOps engineer at a startup. 
The team wants to containerize a simple Python Flask API and serve it behind an Nginx reverse proxy. The goal is to:
Build a Docker image for the backend API.
Run the backend and frontend together using Docker Compose.
Deploy the same app in Docker Swarm on a single node, scaling the backend to multiple replicas.
Tasks

Backend Dockerfile
Write a Flask app (app.py) that returns JSON: {"msg":"Hello from backend"} at /.
Add a requirements.txt (with Flask).
Create a Dockerfile to build the backend image.
Build and run the image locally, then test with curl.
Docker Compose Setup
Create a docker-compose.yml with:
backend → Flask container from your Dockerfile (expose port 5000).
frontend → Nginx container acting as reverse proxy.
Nginx should serve / with a static page and forward /api to the backend
Write a simple nginx.conf to configure reverse proxy.
Run docker-compose up and confirm:
http://localhost:8080/ → Nginx welcome page.
http://localhost:8080/api → Flask backend response.
Docker Swarm Deployment
Initialize Swarm on your machine (docker swarm init).
Create a stack.yml (can reuse Compose file, add deploy settings).
Deploy the stack:
Scale the backend to 3 replicas in the stack file.
Verify load balancing by curling /api multiple times.