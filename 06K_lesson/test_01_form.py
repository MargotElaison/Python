import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    # Настройка драйвера
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )
    yield driver
    # Закрытие браузера после теста
    driver.quit()


def test_form(driver):
    # Открытие страницы
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )

    # Заполнение формы
    fields = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "zip-code": "",  # Оставляем пустым
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    for field_id, value in fields.items():
        if value:
            driver.find_element(By.NAME, field_id).send_keys(value)

    # Нажатие кнопки Submit
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Проверка подсветки Zip code
    zip_code_field = driver.find_element(By.ID, "zip-code")
    assert "alert-danger" in zip_code_field.get_attribute("class"), \
        "Поле Zip code должно быть подсвечено красным (ошибка)"

    # Проверка подсветки остальных полей
    green_fields = ["first-name", "last-name", "address", "e-mail", "phone",
                    "city", "country", "job-position", "company"]

    for field_id in green_fields:
        field = driver.find_element(By.ID, field_id)
        assert "alert-success" in field.get_attribute("class"), \
            f"Поле {field_id} должно быть подсвечено зеленым (успех)"
