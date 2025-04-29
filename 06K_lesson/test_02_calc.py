import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    # Настройка драйвера
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )
    yield driver
    # Закрытие браузера после теста
    driver.quit()


def test_calc(driver):
    # Открытие страницы
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )

    # Тестовые данные
    calc_timeout = "45"
    keys_to_press = "7+8="
    expected_result = "15"

    # Устанавливаем задержку
    delay_field = driver.find_element(By.ID, "delay")
    delay_field.clear()
    delay_field.send_keys(calc_timeout)

    # Поле вывода
    screen = driver.find_element(By.CSS_SELECTOR, "div.screen")

    # Нажимаем кнопки с небольшими паузами между нажатиями
    for key in keys_to_press:
        button = driver.find_element(By.XPATH, f"//span[text()='{key}']")
        button.click()

    # Ожидаем результат с запасом времени
    try:
        WebDriverWait(driver, float(calc_timeout)).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, "div.screen"),
                expected_result
            )
        )
    except TimeoutException:
        pytest.fail(
            f"Результат '{expected_result}' не появился "
            f"в течение {calc_timeout} секунд"
        )

    # Финишная проверка результата
    assert screen.text == expected_result, \
        f"Ожидался результат '{expected_result}', но получили '{screen.text}'"
