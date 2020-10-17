import pytest

# リダイレクトの確認


def test_is_pass_successful_for_habit_list(client):
    response = client.get('/habitList/')
    assert response.status_code == 302


def test_is_pass_successful_for_habit_create(client):
    response = client.get('/habitCreate/')
    assert response.status_code == 200


def test_is_pass_successful_for_signup(client):
    response = client.get('/signup/')
    assert response.status_code == 200


def test_is_pass_successful_for_login(client):
    response = client.get('/login/')
    assert response.status_code == 200


def test_is_pass_successful_for_logout(client):
    response = client.get('/logout/')
    assert response.status_code == 302
