from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    
    BASKET_LINK = (By.CSS_SELECTOR, 'span a')

class MainPageLocators:
    pass
    
class BasketPageLocators:
    MESSAGE_EMPTY = (By.CSS_SELECTOR, '#content_inner > p')
    BASKET_ITEMS= (By.CSS_SELECTOR, '.basket-items')
    
class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
    REGISTER_EMAIL = (By.NAME, 'registration-email')
    REGISTER_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_PASSWORD_REPEAT = (By.CSS_SELECTOR, '#id_registration-password2')
    SUBMIT_REGISTER = (By.NAME, 'registration_submit')
    
class ProductPageLocators:
    ADD_TO_BASKET_FORM = (By.CSS_SELECTOR, ".btn-add-to-basket")
    
    NAME_PRODUCT_BEFORE = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_PRODUCT_BEFORE = (By.CSS_SELECTOR, ".product_main .price_color")
    NAME_PRODUCT_AFTER = (By.CSS_SELECTOR, ".alert:nth-child(1) strong")
    PRICE_PRODUCT_AFTER = (By.CSS_SELECTOR, ".alert:nth-child(3) strong")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    

