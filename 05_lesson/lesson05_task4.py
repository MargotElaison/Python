from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time


def main():
    # Настройка драйвера Firefox
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    # Переход на страницу
    driver.get("https://the-internet.herokuapp.com/login")

    # Ввод логина
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("tomsmith")
    time.sleep(2)

    # Ввод пароля
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("SuperSecretPassword!")
    time.sleep(2)

    # Нажатие кнопки Login
    login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
    login_button.click()

    # Вывод текста из зеленой плашки
    flash_message = driver.find_element(By.ID, "flash")
    print("Сообщение после входа:", flash_message.text)

    # Закрытие браузера
    driver.quit()


if __name__ == "__main__":
    main()
