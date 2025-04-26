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
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
        )

        # Ожидание загрузки всех картинок
        WebDriverWait(driver, 10).until(
            ec.invisibility_of_element_located((By.ID, "spinner"))
        )

        # Получение src у 3-ей картинки
        third_image = (driver.find_element
                       (By.CSS_SELECTOR, "#image-container img:nth-child(3)")
                       )
        src_attribute = third_image.get_attribute("src")

        # Вывод значения в консоль
        print(src_attribute)

    finally:
        # Закрытие браузера
        driver.quit()


if __name__ == "__main__":
    main()
