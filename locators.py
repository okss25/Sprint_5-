from selenium.webdriver.common.by import By


class LocatorsPage:
    Регистрация:
    name_field = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    email_field = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    password_field = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    register_button = (By.XPATH, "//button[text()='Зарегистрироваться']")
    error_message = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")
    Вход:
    login_button_main = (By.XPATH, "//button[text()='Войти в аккаунт']")
    login_button_profile = (By.XPATH, "//a[@href='/login']")
    login_button_register = (By.XPATH, "//a[text()='Войти']")
    login_button_forgot = (By.XPATH, "//a[text()='Восстановить пароль']")
    email_field = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    password_field = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    login_submit_button = (By.XPATH, "//button[text()='Войти']")
    Личный
    кабинет / Конструктор:
    profile_link = (By.XPATH, "//a[@href='/account']")
    constructor_link = (By.XPATH, "//p[text()='Конструктор']")
    stellar_logo = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]")
    logout_button = (By.XPATH, "//button[text()='Выйти']")
    Разделы
    конструктора:
    bun_tab = (By.XPATH, "//span[text()='Булки']")
    sauce_tab = (By.XPATH, "//span[text()='Соусы']")
    filling_tab = (By.XPATH, "//span[text()='Начинки']")