# Todo API

A simple RESTful **Todo List API** built with **FastAPI**, **SQLAlchemy**, and **SQLite**. It supports creating, reading, updating, and deleting tasks, and includes a small pytest suite for endpoint testing.

---

## Features

- Create new tasks
- View all tasks
- View a single task by ID
- Update an existing task
- Delete tasks
- Health check endpoint
- SQLite database by default
- Test suite with isolated test database override

---

## Project Structure

```text
.
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
│   └── test_tasks.py        # API tests
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd todo-api
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

##  Run the API

Start the development server with:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

- `http://127.0.0.1:8000`
- Swagger docs: `http://127.0.0.1:8000/docs`
- ReDoc docs: `http://127.0.0.1:8000/redoc`

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

For tests, the project uses a separate SQLite database override in `tests/test_tasks.py`.

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

This project is open for learning and personal use. You can add a license here if you plan to publish it.

