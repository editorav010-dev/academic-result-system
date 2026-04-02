# EduReport (Academic Result System)

EduReport is a comprehensive, production-ready academic result management system designed to streamline the administration of student data, examinations, marks, and result generation. Built with a modern, high-performance stack, it provides an efficient and scalable way to manage and track educational records.

## Purpose

The primary purpose of EduReport is to digitize and simplify the academic grading and reporting workflows for educational institutions. By consolidating records of students, classes, subjects, exams, and marks into a single platform, it eliminates manual bookkeeping errors and accelerates the process of publishing academic results.

## Key Objectives

- **Centralized Data Management:** Maintain a secure and organized system for tracking students, their classes, enrolled subjects, and scheduled exams.
- **Multi-Institution Support:** Support distinct profiles for traditional Schools and Coaching Centers, accommodating their unique organizational structures.
- **Streamlined Result Processing:** Automate the entry of student marks and the generation of comprehensive academic results.
- **High-Performance & Dynamic UX:** Deliver a fast, responsive, and interactive user interface utilizing Jinja2 templates paired with HTMX, eliminating the complexity of heavy single-page applications.
- **Secure & Scalable Infrastructure:** Leverage asynchronous Python (FastAPI + async SQLAlchemy) and PostgreSQL for robust performance, completely containerized via Docker for reliable deployment.

---

## Tech Stack

| Layer       | Technology                      |
|-------------|---------------------------------|
| **Backend**     | FastAPI · Python 3.11           |
| **Database**    | PostgreSQL 16 · SQLAlchemy 2 (async) |
| **Templates**   | Jinja2 · HTMX                   |
| **Security**    | passlib (bcrypt)                |
| **Infra**       | Docker · Docker Compose         |

## Project Architecture

```text
EduReport/
├── app/
│   ├── main.py            # FastAPI entrypoint & app lifespan
│   ├── config.py          # Environment settings (Pydantic)
│   ├── database.py        # Async DB Engine & session management
│   ├── models/            # SQLAlchemy ORM Models (Users, Students, Classes, Exams, Marks, Profiles)
│   ├── schemas/           # Pydantic schemas for data validation and serialization
│   ├── routes/            # API & View Routers (Auth, Results, Profiles, Students, Subjects, etc.)
│   ├── templates/         # Jinja2 HTML templates enhanced with HTMX for dynamic interactions
│   └── static/            # Static assets (CSS, JS, images)
├── scripts/               # Optional utility scripts (seed_db, test_connection)
├── Dockerfile             # Container configuration for the FastAPI service
├── docker-compose.yml     # Multi-container orchestration (App + DB)
├── requirements.txt       # Python dependencies
└── .env.example           # Example environment variables
```

## Quick Start

### 1. Clone & Configure

```bash
git clone <repo-url>
cd EduReport

# Copy the example environment variables and edit if necessary
cp .env.example .env
```

### 2. Run with Docker Compose

Ensure Docker is installed and running, then build and start the containers:

```bash
docker-compose up --build
```

This spins up two core containers:

| Container         | Description              | Port  |
|-------------------|--------------------------|-------|
| `edureport_web`   | FastAPI application      | 8000  |
| `edureport_db`    | PostgreSQL 16            | 5432  |

*Note: The web container will automatically wait for the PostgreSQL database to be healthy before fully initializing.*

### 3. Verify Deployment

- **Application UI:** [http://localhost:8000](http://localhost:8000)
- **Health Check:** [http://localhost:8000/health](http://localhost:8000/health) → `{"status": "healthy"}`
- **Interactive API Documentation (Swagger):** [http://localhost:8000/docs](http://localhost:8000/docs)

## Environment Variables

EduReport uses the following core environment variables. A complete list is available in `.env.example`.

| Variable            | Description                            | Default (in .env.example)            |
|---------------------|----------------------------------------|--------------------------------------|
| `POSTGRES_USER`     | PostgreSQL authentication username     | `edureport_user`                     |
| `POSTGRES_PASSWORD` | PostgreSQL authentication password     | `edureport_secret`                   |
| `POSTGRES_DB`       | Target database name                   | `edureport_db`                       |
| `DATABASE_URL`      | Full SQLAlchemy async connection URL   | `postgresql+asyncpg://...`           |
| `SECRET_KEY`        | Cryptographic key for sessions/tokens  | `change-me-to-a-random-secret-key`   |

## Local Development (Without Docker)

To run the application locally on your host machine (requires a running PostgreSQL instance):

```bash
# 1. Create a virtual environment and install dependencies
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 2. Set the DATABASE_URL environment variable to point to your local DB
# (You can also define this in a local .env file)

# 3. Start the development server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## License

This project is licensed under the MIT License.
