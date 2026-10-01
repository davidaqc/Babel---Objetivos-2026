from selenium.webdriver.common.by import By


class InputsPage:

    TEXT_INPUTS_TITLE = (By.XPATH, "//h2[text()='Text Inputs']")
    TEXT_INPUT = (By.CSS_SELECTOR, '[data-testid="text-input"]')

    def __init__(self, driver):
        self.driver = driver

    def get_text_inputs_title(self):
        return self.driver.find_element(
            *self.TEXT_INPUTS_TITLE
        ).text

    def enter_text(self, text):
        self.driver.find_element(
            *self.TEXT_INPUT
        ).send_keys(text)

    def get_text_input_value(self):
        return self.driver.find_element(
            *self.TEXT_INPUT
        ).get_attribute("value")
    
    def clear_text(self):
        self.driver.find_element(
            *self.TEXT_INPUT
        ).clear()