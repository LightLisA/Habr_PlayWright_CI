from pages.base import Base
from data.constants import Constants
from Locators.auth import Auth
from data.assertions import Assertions
from playwright.sync_api import Page


class Main(Base):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.assertion = Assertions(page)

    def open_login_page(self):
        self.open("")

    def user_login(self):
        self.input(Auth.USERNAME_INPUT, Constants.login)
        self.input(Auth.PASSWORD_INPUT, Constants.password)
        self.click(Auth.LOGIN_BTN)

    def assertion_login_check(self):
        self.assertion.check_URL("inventory.html", "Wrong URL")
