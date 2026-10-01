from selenium.webdriver.common.by import By


class FormsPage:

    USERNAME_INPUT = (By.CSS_SELECTOR, '[data-testid="login-username"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '[data-testid="login-password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[data-testid="login-submit"]')
    LOGIN_SUCCESS_MESSAGE = (By.XPATH, "//*[contains(text(), 'Login successful! Welcome, tester.')]")
    LOGIN_ERROR_MESSAGE = (By.XPATH, "//*[contains(text(), 'Invalid credentials')]")

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def get_login_success_message(self):
        return self.driver.find_element(*self.LOGIN_SUCCESS_MESSAGE).text

    def get_login_error_message(self):
        return self.driver.find_element(*self.LOGIN_ERROR_MESSAGE).text