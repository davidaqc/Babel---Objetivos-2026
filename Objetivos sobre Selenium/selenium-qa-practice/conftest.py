import pytest
from selenium import webdriver
from pages.home_page import HomePage
from pages.inputs_page import InputsPage
from pages.forms_page import FormsPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://qapracticehub.com/")

    yield driver

    driver.quit()


@pytest.fixture
def home_page(driver):
    return HomePage(driver)


@pytest.fixture
def inputs_page(driver):
    return InputsPage(driver)

@pytest.fixture
def forms_page(driver):
    return FormsPage(driver)