from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):    
    def should_be_not_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            'There are items in basket, but should not be'
    
    def should_be_message_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_EMPTY), \
            'There are not message about empty basket, but should be'