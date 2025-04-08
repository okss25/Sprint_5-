
import
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import random
import string

def generate_random_email(length=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length)) + "@example.com"

def generate_random_password(length=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")  # Запуск в фоновом режиме
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_successful_registration(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(By.XPATH, "//label[text()='Имя']/following-sibling::input").send_keys("TestUser")
    email = generate_random_email()
    driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input").send_keys(email)
    password = generate_random_password(8)
    driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input").send_keys(password)
    driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()
    time.sleep(2)
    assert "login" in driver.current_url

def test_incorrect_password(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(By.XPATH, "//label[text()='Имя']/following-sibling::input").send_keys("TestUser")
    email = generate_random_email()
    driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input").send_keys(email)
    driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input").send_keys("123")
    driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()
    time.sleep(2)
    assert "Некорректный пароль" in driver.page_source