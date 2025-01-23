# Medify Assignment

## 🚀 **Getting Started**

### 📋 Prerequisites
Make sure you have the following installed on your system:
- [Docker Desktop](https://www.docker.com/products/docker-desktop) - for building and running the Docker container
- Python (optional, for testing the application locally)

---

## ⚙️ **Setup Instructions**

### 🔗 Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/nilavanan-ver-4/Medify-Assignment.git
cd Medify-Assignment
```

### 🏗️ Build the Docker Image
Build the Docker image for the Python application:
```bash
docker build -t python-docker-app .
```

### ▶️ Run the Docker Container
Start the Docker container:
```bash
docker run -p 5000:5000 python-docker-app
```
This maps port **5000** of your host to port **5000** inside the container.

Visit the application at **[http://localhost:5000]()**.

---

## 📂 **Project Structure**
```plaintext
Medify-Assignment
├── Dockerfile         # Instructions to build the Docker image
├── code.py            # Main Python script for the application
├── requirements.txt   # Python package dependencies
└── README.md          # Project documentation (this file)
```

---

## ✨ **Customizing the Application**

### 🛠️ Add New Dependencies
If you need additional Python libraries:
1. Add the library names to `requirements.txt`.
2. Rebuild the Docker image:
   ```bash
   docker build -t python-docker-app .
   ```

---

## 🐛 **Troubleshooting**

### ❌ **Container Exits Immediately**
- **Cause**: Application errors or incorrect setup.
- **Solution**: Check container logs:
  ```bash
  docker logs <container_id>
  ```

### ⚠️ **Port Already in Use**
- **Cause**: Another process is using port 5000.
- **Solution**: Run the container on a different port:
  ```bash
  docker run -p 8080:5000 python-docker-app
  ```
  Access the application at **[http://localhost:8080](http://localhost:8080)**.

---

## 🎯 **Learning Outcomes**
This project highlights:
- Using Docker to containerize Python applications.
- Managing dependencies with `requirements.txt`.
- Building efficient and reproducible Docker images.
- Running and testing applications in isolated environments.

---

## 📧 **Contact Me**
For any questions or feedback, feel free to reach out:
- **Email**: [nilalinuxa4n@gmail.com](mailto:nilalinuxa4n@gmail.com)
- **GitHub**: [nilavanan-ver-4](https://github.com/nilavanan-ver-4)

---

### ⭐️ **Thank You for Exploring the Assignment!**
