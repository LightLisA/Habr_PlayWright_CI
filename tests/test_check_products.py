import allure
import pytest
from pytest_bdd import scenario, given, when, then, parsers
from pages.market_main_page import MarketPage


@allure.suite("Product Verification Suite")
@allure.parent_suite("Main Application Tests")
@allure.sub_suite("Product Details Verification")
@allure.story("Verify product details from the list")
@allure.title('Verify product details')
@allure.description('Test verifying product name, description, and price for various products.')
@pytest.mark.regression
@pytest.mark.usefixtures('user_login')
@scenario('../features/check_products_price_status_name.feature', 'Verify product details')
def test_successful_login():
    pass


@pytest.fixture
def market_page(page):
    return MarketPage(page)


# ------------------ GIVE ------------------
@given('the user is logged in')
def user_logged_in():
    pass  # Фікстура `user_login` вже виконує вхід


# ------------------ WHEN ------------------
@when(parsers.parse('the user navigates to the product page of "{product_name}"'))
def navigate_under_product(market_page, product_name):
    with allure.step(f'Go to under product "{product_name}"'):
        market_page.navigate_to_product(product_name)


# ------------------ THEN ------------------
@then(parsers.parse('the product name should be "{expected_product_name}"'))
def verify_product_name(market_page, expected_product_name):
    with allure.step(f'The product name should be "{expected_product_name}"'):
        market_page.is_product_name_successful(expected_product_name)


@then(parsers.parse('the product description should be "{expected_description}"'))
def verify_product_description(market_page, expected_description):
    with allure.step(f'The product description should be "{expected_description}"'):
        market_page.is_product_description_successful(expected_description)


@then(parsers.parse('the product price should be "{expected_price}"'))
def verify_product_price(market_page, expected_price):
    with allure.step(f'The product price should be "{expected_price}"'):
        market_page.is_product_price_successful(expected_price)

