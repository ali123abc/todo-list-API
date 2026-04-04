from fastapi.testclient import TestClient
from app.main import app
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.base import Base
from app.db.session import get_db


SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Override the get_db dependency to use the test database
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

# Setup and teardown test DB per test
@pytest.fixture()
def client():
    app.dependency_overrides[get_db] = override_get_db
    Base.metadata.create_all(bind=engine)
    with TestClient(app) as c:
        yield c
    Base.metadata.drop_all(bind=engine)

# Helper function to create a task for testing
def create_task(client, title="Test Task", description="Test Description"):
    return client.post("/tasks", json={
        "title": title,
        "description": description
    })

# Generic health check test
def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

# Test create task endpoint
def test_create_task(client):
    response = create_task(client)
    assert response.status_code == 200
    assert "id" in response.json()

# Test get all tasks endpoint
def test_get_all_tasks(client):
    create_task(client)
    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert(len(response.json()) >= 1)

# Test get task by ID endpoint
def test_get_task_by_id(client):
    create = create_task(client, title="Test Get", description="Test Get desc")
    task_id = create.json()["id"]
    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json()["id"] == task_id

# Test update task endpoint
def test_update_task(client):
    create = create_task(client, title="Test Update", description="Test Update desc")
    task_id = create.json()["id"]
    response = client.put(f"/tasks/{task_id}", json={
        "title": "Updated Title",
        "description": "Updated Desc",
        "completed": True})
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Title"
    assert response.json()["description"] == "Updated Desc"
    assert response.json()["completed"] is True

# Test delete task endpoint
def test_delete_task(client):
    create = create_task(client, title="Test Delete", description="Test Delete desc")
    task_id = create.json()["id"]
    response = client.delete(f"/tasks/{task_id}")
    get_response = client.get(f"/tasks/{task_id}")
    assert get_response.status_code == 404

# Test non-existent task retrieval
def test_get_nonexistent_task(client):
    response = client.get("/tasks/999999")
    assert response.status_code == 404  