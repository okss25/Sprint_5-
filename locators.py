from selenium.webdriver.common.by import By

class RegisterPageLocators:
    NAME_FIELD = (By.XPATH, "//*[@id="root"]/div/main/div/div/div/ul/li[1]/div/div/div//input") # Имя
    EMAIL_FIELD = (By.XPATH, "//*[@id="root"]/div/main/div/div/div/ul/li[2]/div/div/div//input") # Email
    PASSWORD_FIELD = (By.XPATH, "//*[@id="root"]/div/main/div/div/div/ul/li[3]/div/div/div//input") # Пароль
    REGISTER_BUTTON = (By.XPATH, "//*[@id="root"]/div/main/div/div/p[1]/a()='Зарегистрироваться']") # Кнопка "Зарегистрироваться"

class LoginPageLocators:
    EMAIL_FIELD = (By.XPATH, "//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input//input") # Email
    PASSWORD_FIELD = (By.XPATH, "//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/div//input") # Пароль
    LOGIN_BUTTON = (By.XPATH, "//*[@id="root"]/div/main/div/form/button()='Войти']") # Кнопка "Войти"

class MainPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[//*[@id="root"]/div/section/div[1]/div/div[2]/p[2]()='Войти в аккаунт']")
    PERSONAL_CABINET_LINK = (By.XPATH, "//*[@id="root"]/div/header/nav/a()='Личный кабинет']")
    CONSTRUCTOR_LINK = (By.XPATH, "//p class="AppHeader_header__linkText__3q_va ml-2"Конструктор</p>()='Конструктор']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выйти']")
    LOGO_LINK = (By.XPATH, "//div[@class='AppHeader_header__logo']/a")
    BUNS_TAB = (By.XPATH, "//*[@id="root"]/div/main/section[1]/div[1]/div[1]/span()='Булки']/parent::div")
    SAUCES_TAB = (By.XPATH, "//*[@id="root"]/div/main/section[1]/div[1]/div[2]/span()='Соусы']/parent::div")
    FILLINGS_TAB = (By.XPATH, "//*[@id="root"]/div/main/section[1]/div[1]/div[3]/span()='Начинки']/parent::div")