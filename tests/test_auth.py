import allure
import pytest
from pytest_bdd import scenario, given, when, then, parsers
from pages.main_page import Main
from data.constants import Constants


@allure.suite("Authentication Suite")
@allure.parent_suite("Main Application Tests")
@allure.sub_suite("User Login Tests")
@allure.feature("Login feature")
@allure.story("Logining under different users")
@allure.title('Successful user login')
@allure.description('Test that user can successfully log in ')
@pytest.mark.smoke
@scenario('../features/login.feature', 'Successful user login')
def test_successful_login():
    pass


@pytest.fixture
def main_page(browser):
    return Main(browser)


@given('the user is on the login page')
def open_login_page(main_page):
    with allure.step('Opening login page'):
        main_page.open_login_page()


@when(parsers.parse('the user enters valid credentials {login} and {password}'))
def enter_credentials(main_page, login, password):
    if login != "AUTH_LOGIN":
        pass
    else:
        login = Constants.login
        password = Constants.password

    with allure.step('User is entering credentials {login} and {password}'):
        main_page.user_login(login, password)


@then(parsers.parse('the user should be logged in {successfully}'))
def verify_login(main_page, successfully):
    with allure.step('User should get successful    message'):
        main_page.assertion_login_check(successfully)
