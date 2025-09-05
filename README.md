# Dockerized Two-Tier Application (Flask + MySQL)

This project demonstrates the containerization of a classic two-tier web application using Docker and Docker Compose. The architecture consists of a Python Flask web application (Tier 1) that connects to and interacts with a MySQL database (Tier 2), all orchestrated within a portable and isolated Docker environment.

---

## Table of Contents
1.  [Project Overview & Architecture](#project-overview--architecture)
2.  [Technology Stack](#technology-stack)
3.  [Getting Started](#getting-started)
    -   [Prerequisites](#prerequisites)
    -   [Installation & Usage](#installation--usage)
4.  [Security Scanning with Docker Scout](#security-scanning-with-docker-scout)
5.  [Key Concepts Demonstrated](#key-concepts-demonstrated)
6.  [Appendix: Server Setup Guide](#appendix-server-setup-guide)

---

## Project Overview & Architecture

This project models a real-world application architecture where a stateless frontend/backend service needs to connect to a stateful database service.

-   **Tier 1 (Web Application):** A simple Flask application that serves an HTML page. It attempts to connect to the database and displays the connection status, proving the link between the two tiers is active.
-   **Tier 2 (Database):** A standard MySQL 8.0 database instance.
-   **Networking:** The two containers communicate over a private, user-defined bridge network automatically created by Docker Compose. The Flask application is able to find the database using its service name (`mysql-db`) as its hostname.

---

## Technology Stack
-   **Backend:** Python / Flask
-   **Database:** MySQL 8.0
-   **Containerization:** Docker
-   **Orchestration:** Docker Compose
-   **Security:** Docker Scout (for vulnerability scanning)
-   **Version Control:** Git & GitHub

---

## Getting Started

### Prerequisites
-   A system with **Git**, **Docker**, and **Docker Compose** installed.
-   You must be logged into Docker Hub via the command line (`docker login`) to use Docker Scout.

> For a complete guide on setting up a fresh Ubuntu server from scratch, see the [**SERVER_SETUP.md**](SERVER_SETUP.md) file.

### Installation & Usage
The entire application stack is managed by Docker Compose, making it incredibly simple to run.

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/graj902/docker-two-tier-app.git
    cd docker-two-tier-app
    ```

2.  **Build and Run the Application:**
    This single command will build the Flask application image, pull the MySQL image, and start both containers in the correct order.
    ```bash
    docker compose up --build -d
    ```

3.  **Access the Application:**
    Once the containers are running, you can access the Flask web application in your browser at:
    `http://localhost:5000` (or `http://<your-server-ip>:5000`)

    You should see a message confirming a successful database connection.

4.  **Stopping the Application:**
    To stop and remove the containers, network, and volumes, run:
    ```bash
    docker compose down
    ```

---

## Security Scanning with Docker Scout
This project incorporates security best practices by scanning the custom-built application image for known vulnerabilities (CVEs).

### How to Run the Scan
After building the image (which `docker compose up --build` does automatically), run the following command:
```bash
# The image name is defined in docker-compose.yml
docker scout cves docker-two-tier-app-flask-app
This will provide a detailed report of any vulnerabilities found within the image's layers and packages.
Key Concepts Demonstrated
Multi-Container Applications: Managing an application composed of multiple, interconnected services.
Container Networking: Using Docker Compose to create a private network, enabling service discovery via hostnames.
Data Persistence: Using Docker volumes (mysql-data) to ensure that database data survives container restarts and removals.
Secure Credential Management: Passing sensitive information (like database passwords) to containers securely using environment variables rather than hardcoding them.
Infrastructure as Code (IaC): Defining the entire application stack (services, networks, volumes) in a single, version-controlled docker-compose.yml file.
Image Optimization & Security: Utilizing a minimal base image (python:3.9-slim) and scanning the final image for vulnerabilities.
Appendix: Server Setup Guide
A detailed, step-by-step guide for preparing a new Ubuntu server to run this project is available in the SERVER_SETUP.md file.
code
Code
**(Stop copying here)**

---

### Final Step: Commit Your Final Documentation

This is a huge improvement. This `README.md` is now a complete, professional document that thoroughly explains your project.
