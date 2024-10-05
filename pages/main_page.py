import allure

from pages.base import Base
# from data.constants import Constants
from Locators.auth import Auth
from data.assertions import Assertions
from playwright.sync_api import Page


class Main(Base):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.assertion = Assertions(page)

    @allure.step("Opening login page")
    def open_login_page(self):
        self.open("")

    @allure.step("Login in as user")
    def user_login(self, login, password):
        self.input(Auth.USERNAME_INPUT, login)
        self.input(Auth.PASSWORD_INPUT, password)
        self.click(Auth.LOGIN_BTN)

    @allure.step("Check that login was successful")
    def assertion_login_check(self):
        self.assertion.check_URL("inventory.html", "Wrong URL")

    def assertion_login_warning_check(self):
        expect_result = "Epic sadface: Sorry, this user has been locked out."
        self.assertion.have_text(Auth.LOGIN_ERROR_MESSAGE, expect_result,
                                 f"Message does not match: \nER:{expect_result} \nAR: {Auth.LOGIN_ERROR_MESSAGE}")
