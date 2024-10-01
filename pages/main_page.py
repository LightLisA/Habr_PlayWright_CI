from pages.base import Base
from data.constants import Constants
from Locators.auth import Auth
from data.assertions import Assertions
from playwright.sync_api import Page


class Main(Base):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.assertion = Assertions(page)

    def user_login(self):
        print(f"\n\n === User Login case")
        self.open("")
        print(f"1. Open page -  {self.page}")
        self.input(Auth.USERNAME_INPUT, Constants.login)
        print(f"2. Enter User name")
        self.input(Auth.PASSWORD_INPUT, Constants.password)
        print(f"3. Enter User password")
        self.click(Auth.LOGIN_BTN)
        print(f"4. Check page after click -  {self.page} \n\n")
        self.assertion.check_URL("inventory.html", "Wrong URL")
