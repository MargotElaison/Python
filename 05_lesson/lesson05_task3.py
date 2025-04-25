import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


def main():
    # Настройка драйвера Firefox
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    # Переход на страницу
    driver.get("https://the-internet.herokuapp.com/inputs")

    # Ввод текста "Sky" в поле
    input_field = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
    input_field.send_keys("Sky")
    time.sleep(2)

    # Очистка поля
    input_field.clear()

    # Ввод текста "Pro"
    input_field.send_keys("Pro")
    time.sleep(2)

    driver.quit()


if __name__ == "__main__":
    main()
    print("lol kek poluchilos")
