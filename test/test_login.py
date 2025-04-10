
from selenium.webdriver.common.by import By

class TestLogin:
    def test_go_to_profile(self):
        # Кликаем на кнопку "Личный кабинет"
        driver.find_element(*LOGIN_BUTTON).click()

        # Проверяем, что мы перешли на страницу логина (или другую страницу, связанную с личным кабинетом)
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"