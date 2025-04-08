
from selenium.webdriver.common.by import By

def test_login_from_main_page(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
    assert "login" in driver.current_url