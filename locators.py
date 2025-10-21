from selenium.webdriver.common.by import By

# Главная страница
HEADER_MAIN = (By.XPATH, ".//h1[text()='Соберите бургер']")
LOGIN_BUTTON_MAIN = (By.XPATH, ".//button[text()='Войти в аккаунт']")
PERSONAL_ACCOUNT_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']")

# Разделы конструктора
BUNS_SECTION = (By.XPATH, ".//span[text()='Булки']/parent::div")
SAUCES_SECTION = (By.XPATH, ".//span[text()='Соусы']/parent::div")
FILLINGS_SECTION = (By.XPATH, ".//span[text()='Начинки']/parent::div")
ACTIVE_SECTION = (By.CSS_SELECTOR, ".tab_tab_type_current__2BEPc")

# Страница логина
HEADER_LOGIN = (By.XPATH, ".//h2[text()='Вход']")
EMAIL_INPUT_LOGIN = (By.XPATH, ".//input[@name='name']")
PASSWORD_INPUT_LOGIN = (By.XPATH, ".//input[@name='Пароль']")
LOGIN_BUTTON_FORM = (By.XPATH, ".//button[text()='Войти']")
REGISTER_LINK = (By.XPATH, ".//a[text()='Зарегистрироваться']")
RECOVER_PASSWORD_LINK = (By.XPATH, ".//a[text()='Восстановить пароль']")

# Страница регистрации
NAME_INPUT_REGISTER = (By.XPATH, ".//label[text()='Имя']/following-sibling::input")
EMAIL_INPUT_REGISTER = (By.XPATH, ".//label[text()='Email']/following-sibling::input")
PASSWORD_INPUT_REGISTER = (By.XPATH, ".//input[@type='password']")
REGISTER_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")
PASSWORD_ERROR = (By.XPATH, "//p[contains(@class, 'input__error') and contains(text(), 'Некорректный пароль')]")
LOGIN_LINK_FROM_REGISTER = (By.XPATH, ".//a[text()='Войти']")

# Личный кабинет
CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")
LOGO_BUTTON = (By.CSS_SELECTOR, ".AppHeader_header__logo__2D0X2")
PROFILE_LINK = (By.XPATH, ".//a[text()='Профиль']")
LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")

# Страница восстановления пароля
LOGIN_LINK_FROM_RECOVER = (By.XPATH, ".//a[text()='Войти']")

# Кнопка оформления заказа (индикатор успешного входа)
ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")
