import pytest
import requests


class TestAPI:
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! НЕОБХОДИМО ЗАПОЛНИТЬ ДАННЫМИ ОТДЕЛЬНО !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    auth_token =

    # Переменная для id проекта (получается из post запроса на создание)
    id_project = None

    # Базовый URL и название создаваемого проекта
    base_url = 'https://ru.yougile.com'
    project_name = "AutoGenProject"

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

        # Если запрос не выдал 200 или 201, то считаем его неудачным
        assert r.status_code in [200, 201], \
            f"Возникла ошибка при создании проекта! Код ответа не равен 201 или 200!"
        # Записываем полученный id проекта для следующих тестов
        self.__class__.id_project = r.json()["id"]


    @pytest.mark.order(2)
    def test_put(self):
        # Проверяем, что id проекта записан, если нет, то проваливаем тест
        assert self.__class__.id_project is not None, "ID проекта не получен на входе теста!"

        # Параметры для запроса, тут меняем название на название + _edited
        data = {
            "title": self.project_name + "_edited",
        }

        # PUT запрос на изменение проекта
        r = requests.put(
            self.base_url + '/api-v2/projects/' + self.__class__.id_project,
            headers={"Authorization": self.auth_token},
            data=data
        )


        # Если запрос не выдал 200 или 201, то считаем его неудачным
        assert r.status_code in [200, 201], \
            f"Возникла ошибка при создании проекта! Код ответа не равен 201 или 200!"

    @pytest.mark.order(3)
    def test_get(self):
        # Проверяем, что id проекта записан, если нет, то проваливаем тест
        assert self.__class__.id_project is not None, "ID проекта не получен на входе теста!"

        # GET запрос на получение информации о проекте
        r = requests.get(
            self.base_url + '/api-v2/projects/' + self.__class__.id_project,
            headers={"Authorization": self.auth_token},
        )

        # Если запрос не выдал 200 или 201, то считаем его неудачным
        assert r.status_code in [200, 201], \
            f"Возникла ошибка при создании проекта! Код ответа не равен 201 или 200!"


if __name__ == '__main__':
    pytest.main()
