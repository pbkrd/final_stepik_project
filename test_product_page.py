import time

from .pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser, lang_option):
    link = f"http://selenium1py.pythonanywhere.com/{lang_option}/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()

    page.exclude_name_and_price_product_before()

    page.should_be_add_to_basket_form()
    page.go_to_add_to_basket_form()
    page.solve_quiz_and_get_code()

    # time.sleep(3000)
    page.exclude_name_and_price_product_after()
    page.should_be_equel_names_and_prices_of_product()