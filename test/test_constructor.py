import locator
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestMovingToConstructor:
    def test_moving_to_constructor_fillings(self, driver):
        # переход в конструктор "начинок"
        driver.find_element(locator.TestLocators.FILLINGS_ELEMENT_CLICK).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            locators.TestLocators.FILLINGS_ELEMENT_WAIT))

        assert driver.find_element(locator.TestLocators.FILLINGS_ELEMENT).is_displayed(), \
            "Элемент начинок не найден на странице"


    def test_moving_to_constructor_sauces(self, driver):
        # переход в конструктор "соусов"
        driver.find_element(locator.TestLocators.SAUCES_ELEMENT_CLICK).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            locators.TestLocators.SAUCES_ELEMENT_WAIT))

        assert driver.find_element(locator.TestLocators.SAUCES_ELEMENT).is_displayed(), \
            "Элемент соусов не найден на странице"


    def test_moving_to_constructor_rolls(self, driver):
        # объявление элемента
        element = driver.find_element(locator.TestLocators.SAUCES_ELEMENT)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        # переход на конструктор "булок"
        driver.find_element(locator.TestLocators.ROLLS_ELEMENT_CLICK).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            locator.TestLocators.ROLLS_ELEMENT_WAIT))

        assert driver.find_element(locator.TestLocators.ROLLS_ELEMENT).is_displayed(), \
            "Элемент булок не найден на странице"