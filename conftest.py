import sys
import os
import pytest
import requests
from urls import BASE_URL
from endpoints import Endpoints
from helpers import generate_unique_user, delete_courier

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

@pytest.fixture
def courier():
    user = generate_unique_user()
    response = requests.post(BASE_URL + Endpoints.CREATE_COURIER_EP, json=user)
    assert response.status_code == 201

    login_data = {"login": user["login"], "password": user["password"]}

    login_resp = requests.post(BASE_URL + Endpoints.LOGIN_COURIER_EP, json=login_data)
    assert login_resp.status_code == 200
    courier_id = login_resp.json()["id"]

    yield {"id": courier_id, **login_data}

    delete_resp = delete_courier(courier_id)
    assert delete_resp.status_code == 200
