# fullstack-aws-ci-cd

## Description
Industry-style CI/CD practice project using Docker containers for both the application and database. The pipeline is automated with GitHub Actions and deployed on AWS EC2, simulating real-world production DevOps workflows.

## Tech Stack
- Docker & Docker Compose
- GitHub Actions (CI/CD)
- AWS EC2
- Fullstack Application (Frontend + Backend)
- Containerized Database

## Project Structure
- `.github/workflows` — GitHub Actions CI/CD pipelines  
- `backend` — Backend application  
- `frontend` — Frontend application  
- `.dockerignore` — Docker ignore rules  
- `.env.example` — Sample environment variables  
- `Dockerfile` — Application Docker configuration  
- `docker-compose.yml` — Multi-container setup (app + database)

## CI/CD Workflow
- Code push triggers GitHub Actions
- Automated build and testing
- Docker images built and deployed to AWS EC2
- Containers managed using Docker Compose

## Purpose
This project was built as **hands-on, industry-grade DevOps practice**, focusing on containerization, CI/CD automation, and cloud deployment using real production-style workflows.

## 👤 Author Note
Created by **Injamul (AI/ML Engineer)** as part of continuous learning and practical experience in cloud-native architecture, DevOps, and production deployment pipelines.
