
from fastapi import status

class TestCreateTask:
    # Test create task endpoint
    def test_create_task(self, create_task):
        response = create_task()
        assert response.status_code == status.HTTP_201_CREATED
        json = response.json()
        assert "id" in json
        assert isinstance(json["id"], int)  

    # Test create task with custom values
    def test_create_task_custom_values(self, client):
        response = client.post("/tasks", json={
            "title": "Custom Title",
            "description": "Custom Description"
        })
        assert response.status_code == status.HTTP_201_CREATED
        json = response.json()
        assert json["title"] == "Custom Title"
        assert json["description"] == "Custom Description"

    # Test create task with missing title
    def test_create_task_missing_title(self, client):
        response = client.post("/tasks", json={
            "description": "Test Description"
        })
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT

    # Test create task with invalid Title
    def test_create_task_invalid_title(self, client):
        response = client.post("/tasks", json={
            "title": 123542,
            "description": "Test Description"
        })
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT

    # Test create task with empty title
    def test_create_task_empty_title(self, client):
        response = client.post("/tasks", json={
            "title": "",
            "description": "Test Description"
        })
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT

    # Test create task with empty request body
    def test_create_task_empty_body(self, client):
        response = client.post("/tasks", json={})
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT    