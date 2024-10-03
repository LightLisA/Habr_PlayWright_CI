import pytest
from pytest_bdd import scenario, given, when, then
from pages.main_page import Main


@pytest.mark.smoke
@scenario('../features/login.feature', 'Successful user login')
def test_successful_login():
    pass


@pytest.fixture
def main_page(browser):
    return Main(browser)


@given('the user is on the login page')
def open_login_page(main_page):
    main_page.open_login_page()


@when('the user enters valid credentials')
def enter_credentials(main_page):
    main_page.user_login()


@then('the user should be logged in successfully')
def verify_login(main_page):
    main_page.assertion_login_check()
