from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_basket_form(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_FORM), \
            "Adding basket form is not presented"

    def go_to_add_to_basket_form(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_FORM)
        link.click()
    
    def exclude_name_and_price_product_before(self):
        self.name_before = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_BEFORE).text
        self.price_before = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_BEFORE).text
        
    def exclude_name_and_price_product_after(self):
        self.name_after = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_AFTER).text
        self.price_after = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_AFTER).text

    def should_be_equel_names_product(self):
        assert self.name_before == self.name_after, \
            'Names of product before and after are not equal'

    def should_be_equel_prices_product(self):
        # print(self.price_before)
        # print(self.price_after)
        assert self.price_before == self.price_after, \
            'Prices of product before and after are not equal'

    def should_be_equel_names_and_prices_of_product(self):
        self.should_be_equel_names_product()
        self.should_be_equel_prices_product()