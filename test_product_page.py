import pytest
import time
from .pages.product_page import ProductPage, ProductPageLocators
from .pages.login_page import LoginPage



# @pytest.mark.parametrize('link_id', [0, 1, 2, 3, 4, 5, 6,
#                                   pytest.param(7, marks=pytest.mark.xfail),
#                                   8, 9])
# def test_guest_can_add_product_to_basket(browser, link_id):
#     link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link_id}"
#     page = ProductPage(browser, link)
#     page.open()
#
#     page.go_to_add_to_basket_form()
#     page.solve_quiz_and_get_code()
# 
#     page.should_be_equel_names_and_prices_of_product()
#
# @pytest.mark.xfail
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.go_to_add_to_basket_form()
#     assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
#         'There is success message after adding product to basket, but should not be'
#
# def test_guest_cant_see_success_message(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()
#     assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
#         'There is success message, but should not be'
#
# @pytest.mark.xfail
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.go_to_add_to_basket_form()
#     page.should_disappear_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()