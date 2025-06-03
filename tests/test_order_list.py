import requests
import allure
from endpoints import Endpoints
from urls import BASE_URL


class TestOrderList:

    @allure.title("Получение списка заказов")
    def test_get_order_list_returns_orders_list(self):
        response = requests.get(BASE_URL + Endpoints.GET_ORDER_LIST_EP)
        assert response.status_code == 200
        json_resp = response.json()

        assert "orders" in json_resp, "В ответе отсутствует ключ 'orders'"
        assert isinstance(json_resp["orders"], list), "'orders' не является списком"
