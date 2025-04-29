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


def test_shop(driver):
    # Открытие страницы
    driver.get("https://www.saucedemo.com/")

    # Параметры
    login = "standard_user"
    password = "secret_sauce"
    user_name = "Marko"
    user_surname = "Nikolo"
    user_address = "Somewhere in the world"
    expected_total = "$58.29"

    # Авторизация
    driver.find_element(By.ID, "user-name").send_keys(login)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    # Добавление в корзину
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    # Переход в корзину
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()

    # Checkout
    driver.find_element(By.ID, "first-name").send_keys(user_name)
    driver.find_element(By.ID, "last-name").send_keys(user_surname)
    driver.find_element(By.ID, "postal-code").send_keys(user_address)
    driver.find_element(By.ID, "continue").click()

    # Проверка итогового числа
    total = driver.find_element(By.CSS_SELECTOR, "div.summary_total_label")
    total_result = total.text.replace("Total: ", "")

    assert total_result == expected_total, \
        f"Ожидался результат '{expected_total}', но получили '{total.text}'"
