import pytest


def test_is_successed_for_habit_list(client):
    response = client.get('/habitList/')
    assert response.status_code == 302

