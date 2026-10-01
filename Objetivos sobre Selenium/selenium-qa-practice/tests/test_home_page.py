
def test_page_title(home_page):
    assert home_page.get_page_title() == "QA Practice Hub"


def test_locators_link_is_visible(home_page):
    assert home_page.get_locators_link().is_displayed()
