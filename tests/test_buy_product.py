import pytest
from pytest_bdd import scenario, given, when, then
from pages.market_main_page import MarketPage


@pytest.mark.regression
@pytest.mark.usefixtures('user_login')
@scenario('../features/buy_products.feature', 'Successful buying products')
def test_successful_buying_products():
    pass


@pytest.fixture
def market_page(browser):
    return MarketPage(browser)


@given('the user is logged in')
def user_logged_in():
    pass  # Фікстура `user_login` вже виконує вхід


@when('the user adds a product to the cart')
def add_products_to_cart(market_page):
    market_page.add_to_cart()


@when('the user proceeds to checkout')
def proceed_to_checkout(market_page):
    market_page.checkout()


@then('the product should be successfully purchased')
def verify_purchase(market_page):
    market_page.is_purchase_successful()
