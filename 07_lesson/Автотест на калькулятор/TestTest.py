import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result_screen = (By.CLASS_NAME, "screen")
        self.button_locator_template = "//span[text()='{}']"

    def set_delay(self, delay):
        element = self.driver.find_element(*self.delay_input)
        element.clear()
        element.send_keys(delay)
        time.sleep(1)  # Пауза после ввода

    def click_button(self, button_text):
        locator = (By.XPATH, self.button_locator_template.format(button_text))
        self.driver.find_element(*locator).click()
        # Пауза между нажатиями кнопок, чтобы проконтролировать точность
        time.sleep(0.5)

    def get_result(self):
        time.sleep(45)  # Ожидание вычисления результата
        return self.driver.find_element(*self.result_screen).text


class TestCalculator:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install())
        )
        self.calculator = CalculatorPage(self.driver)
        yield
        self.driver.quit()

    def test_addition_with_delay(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.calculator.set_delay("45")
        self.calculator.click_button("7")
        self.calculator.click_button("+")
        self.calculator.click_button("8")
        self.calculator.click_button("=")

        result = self.calculator.get_result()
        assert result == "15", f"Ожидался результат '15', получено '{result}'"


if __name__ == "__main__":
    pytest.main(["-v"])
