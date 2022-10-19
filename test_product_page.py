import pytest
import time
from .pages.product_page import ProductPage


@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6,
                                  pytest.param(7, marks=pytest.mark.xfail),
                                  8, 9])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)
    page.open()

    page.go_to_add_to_basket_form()
    page.solve_quiz_and_get_code()

    # time.sleep(10)
    page.should_be_equel_names_and_prices_of_product()