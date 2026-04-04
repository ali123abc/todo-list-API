from fastapi import status

class TestUpdateTasks:
    # Test update task endpoint
    def test_update_task(self, client, create_task):
        create = create_task()
        task_id = create.json()["id"]
        response = client.put(f"/tasks/{task_id}", json={
            "title": "Updated Title",
            "description": "Updated Desc",
            "completed": True})
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["title"] == "Updated Title"
        assert data["description"] == "Updated Desc"
        assert data["completed"] is True

    # Test update non-existent task
    def test_update_nonexistent_task(self, client):
        response = client.put("/tasks/999999", json={
            "title": "Updated Title",
            "description": "Updated Desc",
            "completed": True})
        assert response.status_code == status.HTTP_404_NOT_FOUND

    # Test update task with invalid data
    def test_update_task_invalid_data_type(self, client, create_task):
        task = create_task()
        task_id = task.json()["id"]
        response = client.put(f"/tasks/{task_id}", json={
            "title": 12345,
            "description": "Updated Desc",
            "completed": True})
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT