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

def delete_courier(courier_id):
    response = requests.delete(BASE_URL + Endpoints.DELETE_COURIER_EP.format(id=courier_id))
    return response
