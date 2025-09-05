# Docker Two-Tier App with Security Scanning

This project demonstrates how to set up a **two-tier Docker application** (Flask + MySQL) with **Docker Compose** and perform **container image vulnerability scanning** using [Trivy](https://aquasecurity.github.io/trivy/).

---

## 🐳 Install Docker

Follow the official Docker installation guide for Ubuntu:  
👉 [Install Docker on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)

---

## 🔧 Install Docker Compose

Official docs:  
👉 [Install Docker Compose](https://docker-docs.uclv.cu/compose/install/)

Or install manually:

```bash
sudo curl -L "https://github.com/docker/compose/releases/download/1.26.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose


docker-compose version

docker-compose up --build -d

docker logout
docker login
docker-compose down


sudo apt-get install -y wget apt-transport-https gnupg lsb-release
wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | sudo gpg --dearmor -o /usr/share/keyrings/trivy.gpg
echo "deb [signed-by=/usr/share/keyrings/trivy.gpg] https://aquasecurity.github.io/trivy-repo/deb $(lsb_release -sc) main" | sudo tee /etc/apt/sources.list.d/trivy.list
sudo apt-get update
sudo apt-get install -y trivy
trivy --version
trivy image docker-two-tier-app_flask-app:latest


