import data
import locators

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")  # Запуск в фоновом режиме
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_profile_transition(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click()
    time.sleep(2)
    assert "login" in driver.current_url #требуется авторизация