import allure

from pages.base import Base
from Locators.basket_page import Basket
from Locators.market_page import Market
from data.assertions import Assertions
from playwright.sync_api import Page


class MarketPage(Base):
    def __init__(self, page: Page):
        super().__init__(page)
        self.assertions = Assertions(page)

    @allure.step("Adding prodict to the card")
    def add_to_cart(self):
        with allure.step('Choose 1st product in the list'):
            self.click_element_by_index(Market.ADD_TO_CART,
                                        0)  # кликаем по индексу, 0 это значит, что кликаем по первой карточке
        with allure.step('Navigate to basket'):
            self.click(Market.FOLLOW_TO_BASKET)

    @allure.step("Processing checkout with user details")
    def checkout(self, first_name, last_name, zip_value):
        with allure.step('Click [Checkout] button'):
            self.click(Basket.CHECKOUT_BTN)
        with allure.step(f'Enter user 1st name - {first_name}'):
            self.input(Basket.FIRST_NAME, f"{first_name}")
        with allure.step(f'Enter user 2nd name - {last_name}'):
            self.input(Basket.LAST_NAME, f"{last_name}")
        with allure.step(f'Enter user ZIP code - {zip_value}'):
            self.input(Basket.ZIP, f"{zip_value}")
        with allure.step('Click [Continue] button'):
            self.click(Basket.CONTINUE_BTN)
        with allure.step('Click [Finish] button'):
            self.click(Basket.FINISH_BTN)

    @allure.step("Checking the success of the purchase")
    def is_purchase_successful(self):
        self.assertions.have_text(Basket.FINAL_TEXT, "Checkout: Complete!", "no")
