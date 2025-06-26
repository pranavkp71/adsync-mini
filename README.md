# AdSync Mini 

AdSync Mini is a lightweight AdTech backend system built with **Flask**, **PostgreSQL**, and **Docker**. It simulates a simplified ad campaign sync and reporting platform — ideal for showcasing backend, CI/CD, and DevOps skills.

## Features

-  Sync mock campaign data from JSON
-  Calculate CTR (click-through rate) per campaign
-  Automated testing with `pytest` and GitHub Actions
-  Dockerized with PostgreSQL support
-  CI/CD integrated using GitHub Actions
-  Deployable to Render using `render.yaml`

## Tech Stack

- Backend: Flask
- Database: PostgreSQL
- ORM: SQLAlchemy
- DevOps: Docker, Docker Compose
- CI/CD: GitHub Actions
- Deployment: Render

## API Endpoints

| Method | Endpoint     | Description                       |
|--------|--------------|-----------------------------------|
| GET    | `/`          | Health check                      |
| GET    | `/health`    | Returns `{ status: "ok" }`        |
| POST   | `/sync`      | Sync campaigns from `campaigns.json` |
| GET    | `/report`    | View all campaign stats and CTR   |

## Running Tests

```bash
pytest
