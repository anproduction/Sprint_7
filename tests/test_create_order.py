import pytest
import requests
import allure
from endpoints import Endpoints
from urls import BASE_URL


class TestCreateOrder:

    @allure.title("Создание заказа с параметром цвета: {colors}")
    @pytest.mark.parametrize("colors", [
        (["BLACK"]),
        (["GREY"]),
        (["BLACK", "GREY"]),
        ([]),
    ])
    def test_create_order_colors(self, colors):
        payload = {
            "firstName": "Test",
            "lastName": "User",
            "address": "123 Test St",
            "metroStation": 4,
            "phone": "+79270000000",
            "rentTime": 5,
            "deliveryDate": "2025-06-10",
            "comment": "Test order",
            "color": colors
        }

        response = requests.post(BASE_URL + Endpoints.CREATE_ORDER_EP, json=payload)
        assert response.status_code == 201
        json_resp = response.json()
        assert "track" in json_resp
        assert isinstance(json_resp["track"], int)
