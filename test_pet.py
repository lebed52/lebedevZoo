import pytest
import requests
import allure


base_url= "https://swagger.rv-school.ru/api/v3/pet"

@allure.feature("Питомец")
class TestPet:
    @allure.title("Добавление нового питомца")
    def test_add_pet(self):
        with allure.step("Подготовка данных"):
            budy = {
                "id": 10,
                "name": "doggie",
                "category": {
                    "id": 1,
                    "name": "Dogs"
                },
                "photoUrls": [
                    "string"
                ],
                "tags": [
                    {
                        "id": 0,
                        "name": "string"
                    }
                ],
                "status": "available"
            }
        with allure.step("Отправка запроса на создание питомца"):
            response = requests.post(url=base_url, json=budy)
        with allure.step("Проверка статус-код"):
            assert response.status_code == 200