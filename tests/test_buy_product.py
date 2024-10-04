import allure
import pytest
from pytest_bdd import scenario, given, when, then, parsers
from pages.market_main_page import MarketPage


@allure.suite("Authentication Suite")
@allure.parent_suite("Main Application Tests")
@allure.sub_suite("Successful buying products")
@allure.story("Buy first product from the list")
@allure.title('Successful buying products')
@allure.description('Test purchasing products with valid user data.')
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
    with allure.step('Adding product(-s) to the card'):
        market_page.add_to_cart()


@when(parsers.parse('the user proceeds to checkout with "{first_name}" and "{last_name}" and "{zip}"'))
def proceed_to_checkout(market_page, first_name, last_name, zip):
    with allure.step('Entering "{first_name}" and "{last_name}" and "{zip}" values in fields'):
        market_page.checkout(first_name, last_name, zip)


@then('the product should be successfully purchased')
def verify_purchase(market_page):
    with allure.step('Verifying purchase is successful'):
        market_page.is_purchase_successful()
