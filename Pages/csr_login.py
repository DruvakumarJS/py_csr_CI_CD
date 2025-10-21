import time

from Data.Reading_excel import login_locators
from Data.Reading_excel import ngo_locators

from selenium.webdriver.common.by import By
from Library.selenium_wrapper import SeleniumWrapper

locators = login_locators()


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.sel_wrap_obj = SeleniumWrapper(self.driver)

    def userid_field(self):
       self.sel_wrap_obj.enter_text(locators['userid_field'], "DUMCSR001")
       time.sleep(2)

    def password_field(self):
        self.sel_wrap_obj.enter_text(locators['password_field'], "admin")
        time.sleep(2)

    def login_button(self):
        self.sel_wrap_obj.click_on_element(locators['login_button'])
        time.sleep(3)





                 



