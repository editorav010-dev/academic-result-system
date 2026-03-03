# EduReport

Production-ready FastAPI infrastructure skeleton with PostgreSQL, async SQLAlchemy, Jinja2 + HTMX, and Docker.

## Tech Stack

| Layer       | Technology                      |
|-------------|---------------------------------|
| Backend     | FastAPI · Python 3.11           |
| Database    | PostgreSQL 16 · SQLAlchemy 2 (async) |
| Templates   | Jinja2 · HTMX                  |
| Security    | passlib (bcrypt)                |
| Infra       | Docker · Docker Compose         |

## Project Structure

```
EduReport/
├── app/
│   ├── main.py            # FastAPI entrypoint & lifespan
│   ├── config.py           # Pydantic settings
│   ├── database.py         # Async engine & session
│   ├── models/
│   │   └── user.py         # User ORM model + password hashing
│   ├── routes/
│   │   └── home.py         # / and /health endpoints
│   ├── templates/
│   │   └── index.html      # Landing page with HTMX
│   └── static/             # Static assets (CSS, JS, images)
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env.example
└── README.md
```

## Quick Start

### 1. Clone & configure

```bash
git clone <repo-url> && cd EduReport
cp .env.example .env        # edit credentials if needed
```

### 2. Run with Docker Compose

```bash
docker-compose up --build
```

This spins up two containers:

| Container         | Description              | Port  |
|-------------------|--------------------------|-------|
| `edureport_web`   | FastAPI application      | 8000  |
| `edureport_db`    | PostgreSQL 16            | 5432  |

The web container waits for PostgreSQL to be healthy before starting.

### 3. Verify

- **Browser:** [http://localhost:8000](http://localhost:8000)
- **Health check:** [http://localhost:8000/health](http://localhost:8000/health) → `{"status": "healthy"}`

## Environment Variables

| Variable          | Description                    | Default (in .env.example)      |
|-------------------|--------------------------------|-------------------------------|
| `POSTGRES_USER`   | PostgreSQL username            | `edureport_user`              |
| `POSTGRES_PASSWORD` | PostgreSQL password          | `edureport_secret`            |
| `POSTGRES_DB`     | Database name                  | `edureport_db`                |
| `DATABASE_URL`    | SQLAlchemy async connection URL | `postgresql+asyncpg://...`   |
| `SECRET_KEY`      | App secret key                 | `change-me-to-a-random-secret-key` |

## Development

To run without Docker (requires a running PostgreSQL instance):

```bash
pip install -r requirements.txt
# Set DATABASE_URL in your shell or .env
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## License

MIT
