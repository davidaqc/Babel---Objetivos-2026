import time

def test_navigate_to_inputs(home_page, inputs_page):
    home_page.click_inputs()

    assert inputs_page.get_text_inputs_title() == "Text Inputs"

def test_enter_text(home_page, inputs_page):
    home_page.click_inputs()

    inputs_page.enter_text("David")

    assert inputs_page.get_text_input_value() == "David"


def test_clear_text(home_page, inputs_page):
    home_page.click_inputs()

    inputs_page.enter_text("David")
    inputs_page.clear_text()

    assert inputs_page.get_text_input_value() == ""

    #time.sleep(3)