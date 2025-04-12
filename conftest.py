import pytest
from selenium import webdriver
from locators import LocatorsPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()

    yield driver
    driver.quit()

@pytest.fixture
def page():
    page = LocatorsPage()
    return page



