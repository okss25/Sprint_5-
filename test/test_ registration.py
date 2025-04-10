

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import random
import string


def test_successful_registration(self):
    # Генерируем случайные данные для регистрации
    user_name = 'Kitsi'
    email = generate_random_email()
    password = generate_random_password()

    # Заполняем форму регистрации
    self.driver.find_element(*NAME_INPUT).send_keys(user_name)
    self.driver.find_element(*EMAIL_INPUT).send_keys(email)
    self.driver.find_element(*PASSWORD_INPUT).send_keys(password)
    self.driver.find_element(*REGISTER_BUTTON).click()

    # Проверяем, что произошел переход на страницу логина (косвенно подтверждаем успешную регистрацию)
    self.assertEqual(self.driver.current_url, "https://stellarburgers.nomoreparties.site/login")


def test_incorrect_password_error(self):
    # Заполняем форму регистрации с некорректным паролем
    user_name = 'Kitsi'
    email = generate_random_email()
    password = 'Kit1'

    self.driver.find_element(*NAME_FIELD).send_keys(user_name)
    self.driver.find_element(*EMAIL_FIELD ).send_keys(email)
    self.driver.find_element(*PASSWORD_FIELD).send_keys(password)
    self.driver.find_element(*REGISTER_BUTTON).click()

    # Проверяем появление сообщения об ошибке
    self.assertTrue(self.driver.find_element(*ERROR_MESSAGE).is_displayed())