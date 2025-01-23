# Medify-Assignment


## **Getting Started**

### Prerequisites
Ensure you have the following installed on your machine:
- [Docker Desktop](https://www.docker.com/products/docker-desktop)
- Python (optional, for local testing)

---

## **Setup Instructions**

### Clone the Repository
```bash
git clone https://github.com/yourusername/your-repository-name.git
cd your-repository-name
```

### Build the Docker Image
Run the following command to build the Docker image:
```bash
docker build -t python-docker-app .
```

### Run the Docker Container
To start the container, use:
```bash
docker run -p 5000:5000 python-docker-app
```
This maps port 5000 of your host to port 5000 of the container.

---

## **Project Structure**
```
├── Dockerfile
├── code.py
├── requirements.txt
└── README.md
```
- **Dockerfile**: Instructions to build the Docker image.
- **code.py**: The main Python script for your application.
- **requirements.txt**: Contains Python package dependencies.
- **README.md**: Documentation for the project.

---

## **Customizing the Application**

### Add Dependencies
If additional Python libraries are required:
1. Add them to `requirements.txt`.
2. Rebuild the Docker image using `docker build`.

---

## **Troubleshooting**
- **Issue**: Container exits immediately.
  - **Solution**: Check the logs using `docker logs <container_id>`.
- **Issue**: Port already in use.
  - **Solution**: Change the host port in the `docker run` command (e.g., `-p 8080:5000`).

---

## **Learning Outcomes**
This project demonstrates:
- How to containerize a Python application using Docker.
- Dependency management with a `requirements.txt` file.
- Building and running Docker images for isolated environments.

---

## **Contact**
For any questions or suggestions, feel free to contact me:
- **Email**: your-email@example.com
- **GitHub**: [yourusername](https://github.com/yourusername/)
