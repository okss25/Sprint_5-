
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestConstructorSections:
    def test_go_to_buns(self, driver):
        driver.get(сurl_main_site)
        sauces_button = driver.find_element(By.XPATH, "//span[text()='Соусы']/parent::div") # Локатор кнопки "Соусы"
        sauces_button.click()
        fillings_button = driver.find_element(By.XPATH, "//span[text()='Начинки']/parent::div") # Локатор кнопки "Начинки"
        fillings_button.click()
        buns_button = driver.find_element(By.XPATH, "//span[text()='Булки']/parent::div") # Локатор кнопки "Булки"
        buns_button.click()
        active_tab = driver.find_element(By.XPATH, "//div[contains(@class, 'tab_type_current') and .//span[text()='Булки']]") # Локатор активной вкладки "Булки"
        assert active_tab.is_displayed()

    def test_go_to_sauces(self, driver):
        driver.get(сurl_main_site)
        sauces_button = driver.find_element(By.XPATH, "//span[//*[@id="root"]/div/main/section[1]/div[1]/div[2]/span()='Соусы']/parent::div"()='Соусы']/parent::div") # Локатор кнопки "Соусы"
        sauces_button.click()
        active_tab = driver.find_element(By.XPATH, "//div[contains(@class, 'tab_type_current') and .//span[///html/body/div/div/main/section[1]/div[1]/div[2]/span()='Соусы']]") # Локатор активной вкладки "Соусы"
        assert active_tab.is_displayed()

    def test_go_to_fillings(self, driver):
        driver.get(сurl_main_site)
        fillings_button = driver.find_element(By.XPATH, "//span[/html/body/div/div/main/section[1]/div[1]/div[3]()='Начинки']/parent::div") # Локатор кнопки "Начинки"
        fillings_button.click()
        active_tab = driver.find_element(By.XPATH, "//div[contains(@class, 'tab_type_current') and .//span[text()='Начинки']]") # Локатор активной вкладки "Начинки"
        assert active_tab.is_displayed()