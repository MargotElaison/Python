from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def main():
    # Настройка драйвера
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )

    try:
        # Переход на страницу
        driver.get("http://uitestingplayground.com/ajax")

        # Нажатие на синюю кнопку
        # При выполнении заданий использовать sleep() низзя
        blue_button = WebDriverWait(driver, 10).until(
            ec.element_to_be_clickable((By.CSS_SELECTOR, "button#ajaxButton")))
        blue_button.click()

        # Получение текста из зеленой плашки
        green_message = WebDriverWait(driver, 15).until(
            ec.visibility_of_element_located(
                (By.CSS_SELECTOR, "p.bg-success"))
        )
        message_text = green_message.text

        # Вывод текста в консоль
        print(message_text)

    finally:
        # Закрытие браузера
        driver.quit()


if __name__ == "__main__":
    main()
