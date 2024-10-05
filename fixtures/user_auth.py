import allure
import pytest
from pages.main_page import Main
from data.constants import Constants


@pytest.fixture(scope='class')
def user_login(page):
    with allure.step('User login fixture'):
        main_page = Main(page)

        with allure.step('Open login page'):
            main_page.open_login_page()

        with allure.step(f'Enter user name:{Constants.login} and user password:{Constants.password}'):
            main_page.user_login(Constants.login, Constants.password)

        with allure.step('Checking the successful entering'):
            main_page.assertion_login_check()
