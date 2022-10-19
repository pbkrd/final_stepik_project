import time

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "'login' not in url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        
    def register_new_user(self, email, password):
        try:
            email_inp = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
            email_inp.send_keys(email)
            
            pass_inp = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
            pass_inp.send_keys(password)
            
            pass_rep_inp = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_REPEAT)
            pass_rep_inp.send_keys(password)
            
            submit = self.browser.find_element(*LoginPageLocators.SUBMIT_REGISTER)
            submit.click()
        except:
            raise Exception('Can`t authorize user')
    
            