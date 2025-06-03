import requests
import random
import string
from urls import BASE_URL
from endpoints import Endpoints


def generate_unique_user():
    def gen(length=10):
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

    return {
        "login": gen(),
        "password": gen(),
        "firstName": gen()
    }

def create_and_register_courier():
    user = generate_unique_user()
    response = requests.post(BASE_URL + Endpoints.CREATE_COURIER_EP, json=user)
    assert response.status_code == 201
    return {"login": user["login"], "password": user["password"]}