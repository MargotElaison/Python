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
        driver.get("http://uitestingplayground.com/textinput")

        # Ввод текста "SkyPro" в поле ввода
        input_field = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located(
                (By.CSS_SELECTOR, "input#newButtonName")
            )
        )
        input_field.clear()
        input_field.send_keys("SkyPro")

        # Нажатие на синюю кнопку
        blue_button = WebDriverWait(driver, 10).until(
            ec.element_to_be_clickable(
                (By.CSS_SELECTOR, "button#updatingButton")
            )
        )
        blue_button.click()

        # Получение текста кнопки после изменения
        WebDriverWait(driver, 10).until(
            ec.text_to_be_present_in_element(
                (By.CSS_SELECTOR, "button#updatingButton"), "SkyPro"
            )
        )
        button_text = blue_button.text

        # Вывод текста кнопки в консоль
        print(button_text)  # Должно вывести "SkyPro"

    finally:
        # Закрытие браузера
        driver.quit()


if __name__ == "__main__":
    main()
