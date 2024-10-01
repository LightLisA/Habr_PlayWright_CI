import pytest
from pages.main_page import Main


@pytest.fixture(scope='class')
def user_login(browser):
    m = Main(browser)
    print(f"\n=== User Login from user_login.py ===")
    m.user_login()
