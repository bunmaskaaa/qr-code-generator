# 🧾 QR Code Generator (Dockerized)

## 🧠 Overview
This project is a **Dockerized Python QR Code Generator** that creates QR images from a given URL.  
It demonstrates secure containerization practices using a **non-root user**, minimal base image (`python:3.12-slim-bullseye`), and automated CI/CD via **GitHub Actions**.

---

## ⚙️ Features
- Generates QR codes from any URL input.  
- Secure Docker build: non-root user, limited packages, `.dockerignore` optimization.  
- Automated **pytest** unit tests on every commit.  
- CI/CD pipeline using **GitHub Actions** to:
  - Run tests.
  - Build and push Docker images to **DockerHub** automatically.

---

## 🚀 Quick Start

### Run locally
```bash
python main.py --url https://www.njit.edu