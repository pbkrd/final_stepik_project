from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser, lang_option):
    link = f"http://selenium1py.pythonanywhere.com/{lang_option}"
    page = MainPage(browser, link)  
    page.open()
    page.go_to_login_page()