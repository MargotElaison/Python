import pytest
import requests


class TestAPI:
    # Место для токена авторизации (заполняется отдельно перед запуском)
    auth_token = ""

    # Переменная для id проекта (получается из post запроса на создание)
    id_project = None

    # Базовый URL и название создаваемого проекта
    base_url = 'https://ru.yougile.com'
    project_name = "AutoGenProject"

    def _check_status_code(self, response, expected_codes):
        # Вспомогательный метод для проверки кодов ответа
        assert response.status_code in expected_codes, (
            f"Ожидались коды {expected_codes}, получен {response.status_code}"
        )

    @pytest.mark.order(1)
    def test_post(self):
        # Параметры для запроса
        data = {
            "title": str(self.project_name),
            "users": {}
        }

        # POST запрос на создание проекта
        r = requests.post(
            self.base_url + '/api-v2/projects',
            headers={"Authorization": self.auth_token},
            data=data
        )

        # Проверяем успешный статус код
        self._check_status_code(r, [200, 201])

        # Записываем полученный id проекта для следующих тестов
        self.__class__.id_project = r.json()["id"]

    @pytest.mark.order(2)
    def test_post_negative(self):
        # POST запрос без токена авторизации
        r = requests.post(
            self.base_url + '/api-v2/projects',
            headers={"Authorization": ""},
            data={"title": "InvalidProject"}
        )
        self._check_status_code(r, [401])

    @pytest.mark.order(3)
    def test_put(self):
        # Проверяем наличие id проекта
        assert self.__class__.id_project is not None, "ID проекта не получен!"

        # Параметры для запроса
        data = {"title": self.project_name + "_edited"}

        # PUT запрос на изменение проекта
        r = requests.put(
            self.base_url + '/api-v2/projects/' + self.__class__.id_project,
            headers={"Authorization": self.auth_token},
            data=data
        )

        # Проверяем успешный статус код
        self._check_status_code(r, [200, 201])

    @pytest.mark.order(4)
    def test_put_negative(self):
        # PUT запрос с несуществующим ID
        r = requests.put(
            self.base_url + '/api-v2/projects/invalid_project_id',
            headers={"Authorization": self.auth_token},
            data={"title": "InvalidProject"}
        )
        self._check_status_code(r, [404])

    @pytest.mark.order(5)
    def test_get(self):
        # Проверяем наличие id проекта
        assert self.__class__.id_project is not None, "ID проекта не получен!"

        # GET запрос на получение информации о проекте
        r = requests.get(
            self.base_url + '/api-v2/projects/' + self.__class__.id_project,
            headers={"Authorization": self.auth_token},
        )

        # Проверяем успешный статус код
        self._check_status_code(r, [200, 201])

    @pytest.mark.order(6)
    def test_get_negative(self):
        # GET запрос с некорректным форматом ID
        r = requests.get(
            self.base_url + '/api-v2/projects/123-invalid-id-456',
            headers={"Authorization": self.auth_token},
        )
        self._check_status_code(r, [400])


if __name__ == '__main__':
    pytest.main()
