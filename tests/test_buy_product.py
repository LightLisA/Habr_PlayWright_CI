import pytest
from pages.market_main_page import MarketPage


@pytest.mark.regression
@pytest.mark.usefixtures('user_login')
class TestBuyProduct:
    print(f"\n=== TEST BUY PRODUCT from test_buy_product.py ===")

    def test_buy_product(self, browser):
        p = MarketPage(browser)
        p.add_to_cart()
        p.checkout()
