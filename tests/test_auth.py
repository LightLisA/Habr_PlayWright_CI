import pytest
from pytest_bdd import scenario, given, when, then, parsers
from pages.main_page import Main
from data.constants import Constants


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


@when(parsers.parse('the user enters valid credentials {login} and {password}'))
def enter_credentials(main_page, login, password):
    if login != "AUTH_LOGIN":
        pass
    else:
        login = Constants.login
        password = Constants.password

    main_page.user_login(login, password)


@then(parsers.parse('the user should be logged in {successfully}'))
def verify_login(main_page, successfully):
    main_page.assertion_login_check(successfully)
