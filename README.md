# Todo API

A RESTful Todo List API built with FastAPI, featuring a clean layered architecture, full CRUD functionality, and a comprehensive pytest suite.
---

## Features

- Create new tasks
- View all tasks
- View a single task by ID
- Update an existing task
- Delete tasks
- Health check endpoint
- SQLite database by default
- Alembic migrations for schema management
- Test suite with database override and schema setup

--- 

## Architecture

The project follows a clean, layered architecture:

- **Routes**: Handle HTTP requests and responses
- **Services**: Contain business logic
- **Models**: Define database structure using SQLAlchemy
- **Schemas**: Handle request/response validation using Pydantic
- **DB**: Manages database connection and session lifecycle

---

## Tech Stack

- **Python** 
- **FastAPI** 
- **SQLAlchemy** 
- **SQLite** 
- **Alembic** 
- **Pydantic** 
- **Pytest** 
- **Docker** 

---

## Project Structure

```text
.
├── alembic/                # Alembic migration files
├── app/
│   ├── main.py              # FastAPI app entry point
│   ├── db/
│   │   ├── base.py          # SQLAlchemy base
│   │   └── session.py       # DB engine, session, dependency
│   ├── models/
│   │   └── task.py          # Task database model
│   ├── routes/
│   │   └── task.py          # API routes
│   ├── schemas/
│   │   └── task.py          # Request/response schemas
│   └── services/
│       └── task_service.py  # Business logic
├── tests/
│   ├── conftest.py          # Shared pytest fixtures and DB override
│   ├── test_create_tasks.py # Create task endpoint tests
│   ├── test_read_tasks.py   # Read task endpoint tests
│   ├── test_update_tasks.py # Update task endpoint tests
│   └── test_delete_tasks.py # Delete task endpoint tests
├── alembic.ini
├── docker-entrypoint.sh
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/ali123abc/todo-list-API.git
cd todo-list-API
```

### 2. Create and activate a virtual environment

#### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

#### macOS / Linux

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run the API

Apply the database migrations, then start the development server:

```bash
alembic upgrade head
uvicorn app.main:app --reload
```

The API will be available at:

- `http://127.0.0.1:8000`
- Swagger docs: `http://127.0.0.1:8000/docs`
- ReDoc docs: `http://127.0.0.1:8000/redoc`

---
## Running with Docker

Ensure Docker is installed and running.

1. Build the image

```bash
docker build -t todo-api .
```
2. Run the container

```bash
docker run -p 8000:8000 todo-api
```

The container startup script runs `alembic upgrade head` automatically before starting the API.

3. Access the API

http://localhost:8000/docs

If using environment variables use

```bash
docker run -p 8000:8000 -e DATABASE_URL=sqlite:///./todo.db todo-api 
```
---

## Run Tests
The test suite covers CRUD operations, validation, and edge cases using an isolated test database.

Run the test suite with:

```bash
pytest
```

To run a specific test file:

```bash
pytest tests/test_create_tasks.py
```

---

## Database Configuration

The app uses SQLite by default:

```python
sqlite:///./todo.db
```

You can override this with an environment variable:

```powershell
$env:DATABASE_URL="sqlite:///./todo.db"
```

For tests, the project overrides the DB dependency and creates the schema in `tests/conftest.py`.

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/health` | Health check |
| `POST` | `/tasks/` | Create a task |
| `GET` | `/tasks/` | Get all tasks |
| `GET` | `/tasks/{task_id}` | Get a task by ID |
| `PUT` | `/tasks/{task_id}` | Update a task |
| `DELETE` | `/tasks/{task_id}` | Delete a task |


## Task Model

Each task includes:

- `id`
- `title`
- `description`
- `completed`
- `created_at`
- `updated_at`

---

## License

This project is open for learning and personal use.

