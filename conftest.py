
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="session")
def driver():
    options = Options()
    options.add_argument("--window-size=1200,600")
    service = Service("*\Users\Huawei\Web driver\bin\chromedriver-win64\chromedriver-win64")
    driver = webdriver.Chrome(options=options, service=service)
    yield browser
    browser.quit()



