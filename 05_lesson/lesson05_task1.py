from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Настройка драйвера Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Переход на страницу
driver.get("http://uitestingplayground.com/classattr")

# Поиск синей кнопки по классу (она имеет класс 'btn-primary')
blue_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")

# Клик по кнопке
blue_button.click()

input("Нажмите кнопку OK, чтобы подтвердить действие")
