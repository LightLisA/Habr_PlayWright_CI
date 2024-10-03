import pytest
from pages.main_page import Main


@pytest.fixture(scope='class')
def user_login(browser):
    m = Main(browser)
    m.open_login_page()
    m.user_login()
    m.assertion_login_check()
