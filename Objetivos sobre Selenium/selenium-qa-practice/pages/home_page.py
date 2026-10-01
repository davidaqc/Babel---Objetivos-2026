from selenium.webdriver.common.by import By


class HomePage:

    PAGE_TITLE = (By.ID, "page-title")
    LOCATORS_LINK = (By.CSS_SELECTOR, 'a[href="/locators-tutorial"]')
    INPUTS_LINK = (By.CSS_SELECTOR, '[data-testid="nav-inputs"]')
    FORMS_LINK = (By.CSS_SELECTOR, '[data-testid="nav-forms"]')

    def __init__(self, driver):
        self.driver = driver

    def get_page_title(self):
        return self.driver.find_element(*self.PAGE_TITLE).text

    def get_locators_link(self):
        return self.driver.find_element(*self.LOCATORS_LINK)
    
    def click_inputs(self):
        self.driver.find_element(*self.INPUTS_LINK).click()

    def click_forms(self):
        self.driver.find_element(*self.FORMS_LINK).click()