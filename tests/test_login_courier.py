import pytest
import requests
import allure
from endpoints import Endpoints
from urls import BASE_URL
from helpers import create_and_register_courier


class TestLoginCourier:

    @allure.title("Успешный логин курьера")
    def test_login_success(self):
        credentials = create_and_register_courier()
        response = requests.post(BASE_URL + Endpoints.LOGIN_COURIER_EP, json=credentials)
        assert response.status_code == 200
        assert "id" in response.json()
        assert isinstance(response.json()["id"], int)

    @allure.title("Ошибка при логине без обязательного поля")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_login_missing_field(self, missing_field):
        credentials = create_and_register_courier()
        credentials.pop(missing_field)
        response = requests.post(BASE_URL + Endpoints.LOGIN_COURIER_EP, json=credentials)
        assert response.status_code == 400
        assert "message" in response.json()
        assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.title("Ошибка при логине с неверным паролем")
    def test_login_wrong_password(self):
        credentials = create_and_register_courier()
        credentials["password"] = "wrongpass"
        response = requests.post(BASE_URL + Endpoints.LOGIN_COURIER_EP, json=credentials)
        assert response.status_code == 404
        assert "message" in response.json()
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.title("Ошибка при логине несуществующего пользователя")
    def test_login_nonexistent_user(self):
        credentials = {
            "login": "nonexistent_login",
            "password": "nonexistent_password"
        }
        response = requests.post(BASE_URL + Endpoints.LOGIN_COURIER_EP, json=credentials)
        assert response.status_code == 404
        assert "message" in response.json()
        assert response.json()["message"] == "Учетная запись не найдена"
