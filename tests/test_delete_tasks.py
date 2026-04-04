from fastapi import status

class TestDeleteTask:
    # Test delete task endpoint
    def test_delete_task(self, client, create_task):
        task = create_task()
        task_id = task.json()["id"]
        response = client.delete(f"/tasks/{task_id}")
        assert response.status_code == status.HTTP_204_NO_CONTENT
        get_response = client.get(f"/tasks/{task_id}")
        assert get_response.status_code == status.HTTP_404_NOT_FOUND

    # Test delete non-existent task
    def test_delete_nonexistent_task(self, client):
        response = client.delete("/tasks/999999")
        assert response.status_code == status.HTTP_404_NOT_FOUND    

    # Test delete task twice
    def test_delete_task_twice(self, client, create_task):
        task = create_task()
        task_id = task.json()["id"]
        response = client.delete(f"/tasks/{task_id}")
        assert response.status_code == status.HTTP_204_NO_CONTENT
        second_response = client.delete(f"/tasks/{task_id}")
        assert second_response.status_code == status.HTTP_404_NOT_FOUND