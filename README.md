# Lucid test task


## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Launch](#launch)


## Features

- **User Authentication**: Signup and login endpoints with JWT-based authentication.
- **CRUD Operations**: Create, read, and delete posts.
- **Caching**: In-memory caching for efficient data retrieval.
- **Dockerized Deployment**: Docker and Docker Compose for containerized application setup.
- **Auto-migrations**: Auto-migrations on each reload (also from Makefile available)
## Requirements

- Docker
- Docker Compose

## Launch
```commandline
docker compose up --build -d
```