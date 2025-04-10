

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class TestRegistration(self):

    def tearDown(self):
        self.driver.quit()

    def test_successful_registration(self):
        email = 'K12345678899@ya.ru'
        password = 'Kit123456'

        self.driver.find_element(*LOCATOR_NAME_FIELD).send_keys("Test User")
        self.driver.find_element(*LOCATOR_EMAIL_FIELD).send_keys(email)
        self.driver.find_element(*LOCATOR_PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*LOCATOR_REGISTER_BUTTON).click()

        # Добавляем явное ожидание перехода на страницу логина (или любой другой элемент)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LOCATOR_LOGIN_EMAIL_INPUT)
        )
