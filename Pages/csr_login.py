import time
from Data.Reading_excel import login_locators
from Library.selenium_wrapper import SeleniumWrapper

locators = login_locators()

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.sel_wrap_obj = SeleniumWrapper(self.driver)

    def userid_field(self):
        username = "DUMCSR001"
        self.sel_wrap_obj.enter_text(locators['userid_field'], username)
        time.sleep(2)
        return username  # return for logging

    def password_field(self):
        password = "admin"
        self.sel_wrap_obj.enter_text(locators['password_field'], password)
        time.sleep(2)
        return password  # return for logging

    def login_button(self):
        self.sel_wrap_obj.click_on_element(locators['login_button'])
        time.sleep(3)





                 



