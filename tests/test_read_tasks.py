
from fastapi import status

class TestGetAllTasks:
    # Test get all tasks endpoint
    def test_get_all_tasks(self,client, create_task):
        create_task()
        response = client.get("/tasks")

        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert isinstance(data, list)
        assert(len(data) == 1)

    # Test get all tasks with no tasks
    def test_get_all_tasks_empty(self, client):
        response = client.get("/tasks")

        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 0    

class TestGetTaskById:
    # Test get task by ID endpoint
    def test_get_task_by_id(self, client, create_task):
        task = create_task()
        task_data = task.json()
        task_id = task_data["id"]
        response = client.get(f"/tasks/{task_id}")

        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["id"] == task_id
        assert data["title"] == task_data["title"]

    # Test non-existent task retrieval
    def test_get_nonexistent_task(self, client):
        response = client.get("/tasks/999999")

        assert response.status_code == status.HTTP_404_NOT_FOUND  
