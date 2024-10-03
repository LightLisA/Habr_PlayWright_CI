import pytest
from pages.main_page import Main
from data.constants import Constants


@pytest.fixture(scope='class')
def user_login(browser):
    m = Main(browser)
    m.open_login_page()
    m.user_login(Constants.login, Constants.password)
    m.assertion_login_check("YES")
