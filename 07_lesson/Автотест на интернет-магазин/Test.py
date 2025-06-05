import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com")

    def enter_credentials(self, username: str, password: str):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        ).send_keys(username)

        self.driver.find_element(By.ID, "password").send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, "login-button").click()
        return InventoryPage(self.driver)


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("inventory.html")
        )

    def add_item_to_cart(self, item_name: str):
        item_button = f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button"
        self.driver.find_element(By.XPATH, item_button).click()

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        return CartPage(self.driver)


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("cart.html")
        )

    def checkout(self):
        self.driver.find_element(By.ID, "checkout").click()
        return CheckoutPage(self.driver)

    def verify_item_in_cart(self, item_name: str) -> bool:
        try:
            self.driver.find_element(
                By.XPATH,
                f"//div[@class='inventory_item_name' and text()='{item_name}']"
            )
            return True
        except Exception:
            return False


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("checkout-step-one.html")
        )

    def fill_shipping_info(self, first_name: str, last_name: str, postal_code: str):
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)

    def continue_to_overview(self):
        self.driver.find_element(By.ID, "continue").click()
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("checkout-step-two.html")
        )

    def get_total_price(self) -> str:
        return self.driver.find_element(By.CLASS_NAME, "summary_total_label").text


if __name__ == "__main__":
    driver = webdriver.Chrome()

    try:
        login_page = LoginPage(driver)
        login_page.enter_credentials("standard_user", "secret_sauce")
        inventory_page = login_page.click_login()
        time.sleep(5)

        # Добавление товара
        inventory_page.add_item_to_cart("Sauce Labs Backpack")

        # Переход в корзину
        cart_page = inventory_page.go_to_cart()
        time.sleep(5)

        # Проверка товара в корзине
        if cart_page.verify_item_in_cart("Sauce Labs Backpack"):
            print("Товар успешно добавлен в корзину!")
        else:
            print("Ошибка: товар не найден в корзине")

    finally:
        driver.quit()
