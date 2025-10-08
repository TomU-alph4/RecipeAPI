# RecipeAPI

## Summary 

RecipeAPI is an open source API where users can access recipe inspiration base don what they have in their kitchen.

The API will leverage AI/ML to save users having to input everything they have.

---

## Overview

- use users preferences and previous usage to recommend new recipes.
- AI tooling to scan receipts and images to work out what ingredients the user has.
- scale easily across cloud environments

---

## Key Features

- **JWT Authentication** - user registration, login and role based permissions.
- **API** - secure way to submit applications and retrieving applications.
- **Recommendation Engine** - AI driven recommendations.
- **Cloud Ready Deployment** - Dockerised and compatible with serverless platforms
- **Open Source Documentation** - fully documented using FastAPI’s built in Swagger UI.

---

## 🧩 Tech Stack
| Layer | Technology |
|-------|-------------|
| Framework | [FastAPI](https://fastapi.tiangolo.com/) |
| Database | PostgreSQL + SQLModel |
| Authentication | JWT (python-jose) |
| AI/ML | scikit-learn / Hugging Face pipeline |
| Infrastructure | Docker, Docker Compose |
| Testing | pytest, pytest-asyncio |
| CI/CD | GitHub Actions |

---

## Usage
