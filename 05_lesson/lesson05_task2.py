from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Настройка драйвера, если вдруг его нет
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:

    # Переход на страницу
    driver.get("http://uitestingplayground.com/dynamicid")

    # Поиск и клик по синей кнопке (используем CSS-селектор)
    blue_button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
    blue_button.click()

    print("Кнопка успешно нажата!")

finally:

    # Закрытие браузера
    driver.quit()
