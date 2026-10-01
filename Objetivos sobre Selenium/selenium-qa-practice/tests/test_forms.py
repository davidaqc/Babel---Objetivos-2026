
def test_valid_login(home_page, forms_page):
    home_page.click_forms()

    forms_page.enter_username("tester")
    forms_page.enter_password("password123")
    forms_page.click_login()

    assert forms_page.get_login_success_message() == "Login successful! Welcome, tester."

def test_invalid_login(home_page, forms_page):
    home_page.click_forms()

    forms_page.enter_username("wrong_user")
    forms_page.enter_password("wrong_password")
    forms_page.click_login()

    assert forms_page.get_login_error_message() == "Invalid credentials. Try username: tester, password: password123"