import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Data.Reading_excel import ngo_locators
from Library.selenium_wrapper import SeleniumWrapper

locators = ngo_locators()
class NgoCreatePage:
    def __init__(self, driver):
        self.driver = driver
        self.sel_wrap_obj = SeleniumWrapper(driver)
        self.wait = WebDriverWait(driver, 15)  # Explicit wait for elements

        # using Excel sheet

    # def enter_ngo_name1(self):
    #         self.sel_wrap_obj.enter_text(locators['ngo_name'], "Mytri")
    #         time.sleep(2)
    #
    # def select_type_of_ngo1(self):
    #         self.sel_wrap_obj.click_on_element(locators['ngo_type'])
    #         time.sleep(2)
    #
    # def check_empelled_partner(self):
    #         self.sel_wrap_obj.click_on_element(locators['empelled1'])
    #         time.sleep(2)
    #
    # def enter_vendor_code(self):
    #         self.sel_wrap_obj.enter_text(locators['vendor_code'], "UIy654")
    #         time.sleep(2)

    def enter_ngo_name1(self):
        name = "My NGO Name"
        self.sel_wrap_obj.enter_text(locators['ngo_name'], name)
        time.sleep(1)
        return name

    def select_type_of_ngo1(self):
        self.sel_wrap_obj.click_on_element(locators['ngo_type'])
        time.sleep(2)

    def check_empelled_partner(self):
        self.sel_wrap_obj.click_on_element(locators['empelled1'])
        time.sleep(1)
        return True  # just indicate it was checked

    def enter_vendor_code(self):
        code = "V1234"
        self.sel_wrap_obj.enter_text(locators['vendor_code'], code)
        time.sleep(1)
        return code

    def select_multiselect(self):
            self.sel_wrap_obj.select_multiple_options(locators['thematic_area'], ["Disaster Relief","Sports","Environment"])
            time.sleep(2)

    def date_picker(self):
             date_input = self.wait.until(EC.element_to_be_clickable(locators['incorporation']))
             self.driver.execute_script("arguments[0].value = arguments[1];", date_input, "2024-03")
             self.driver.execute_script("arguments[0].dispatchEvent(new Event('change'))", date_input)
             time.sleep(2)

    def enter_registration_details(self):
            self.sel_wrap_obj.enter_text(locators['csr_certificate_no'], "CSR123456789")
            self.sel_wrap_obj.enter_text(locators['g80_number'], "1234567890123456")
            self.sel_wrap_obj.enter_text(locators['a12_number'], "987653210987654323")
            time.sleep(2)

    def select_dropdown(self):
            self.sel_wrap_obj.select_from_dropdown_by_value(locators['g80_validity'], "AY : 2026-2027")
            self.sel_wrap_obj.select_from_dropdown_by_value(locators['a12_validity'], "AY : 2028-2029")
            time.sleep(2)

    def enter_contact_details(self):
            self.sel_wrap_obj.enter_text(locators['pan'], "FNGPS1234H")
            time.sleep(2)
            self.sel_wrap_obj.enter_text(locators['contacts_name'], "Caroline")
            time.sleep(2)
            self.sel_wrap_obj.enter_text(locators['contacts_designation'], "Developer")
            time.sleep(2)
            self.sel_wrap_obj.enter_text(locators['contacts_email'], "swathi@gmail.com")
            time.sleep(2)
            self.sel_wrap_obj.enter_text(locators['contacts_mobile'], "2345678918")
            time.sleep(2)
            self.sel_wrap_obj.enter_text(locators['signatory_name'], "Chandana")
            time.sleep(2)
            self.sel_wrap_obj.enter_text(locators['signatory_designation'], "Tester")
            time.sleep(2)
            self.sel_wrap_obj.enter_text(locators['signatory_email'], "chandana@gmail.com")
            time.sleep(2)
            self.sel_wrap_obj.enter_text(locators['signatory_mobile'], "9867546389")
            time.sleep(2)
            self.sel_wrap_obj.enter_text(locators['acccount_name'], "Sufi")
            time.sleep(2)
            self.sel_wrap_obj.enter_text(locators['bank_name'], "State Bank")
            time.sleep(2)
            self.sel_wrap_obj.enter_text(locators['branch_name'], "Kolkata Nagar")
            time.sleep(2)
            self.sel_wrap_obj.enter_text(locators['account_number'], "987653210987654323")
            time.sleep(2)
            self.sel_wrap_obj.enter_text(locators['ifsc'], "HDFC5678953")
            time.sleep(2)

    def submit_form(self):

     wait = WebDriverWait(self.sel_wrap_obj.driver, 10)
     submit_button = wait.until(EC.element_to_be_clickable(locators['ngoSubmit']))
     self.sel_wrap_obj.driver.execute_script("arguments[0].click();", submit_button)


    #**Locators**
    # locators = {
    #     "ngo_name": (By.XPATH, '//input[@id="ngo_name"]'),
    #     "type_of_ngo": (By.XPATH, '//*[@id="inlineRadio2"]'),
    #     "empelled_partner": (By.XPATH, '//*[@id="empelled1"]'),
    #     "vendor_code": (By.XPATH, '//input[@id="vendor_code"]'),
    #     "thematic": (By.ID,'thematic_area'),
    #     'incorporation': (By.NAME, 'incorporation'),  # Clickable calendar button
    #     'month_option': "//option[@value='{}']",   # Dynamic XPath for selecting a date
    #     "csr_certificate_no": (By.NAME, 'csr_certificate_no'),
    #     "g_registration_number": (By.NAME, 'g80_number'),
    #     "g80_validity": (By.NAME, "g80_validity"),  # Dropdown locator
    #     "a12_validity": (By.NAME, "a12_validity"),  # Dropdown locator
    #     "a_registration_number": (By.NAME, 'a12_number'),
    #     "pan": (By.NAME, 'pan'),
    #     "contact_name": (By.NAME, 'contacts_name'),
    #     "designation": (By.NAME, 'contacts_designation'),
    #     "email": (By.NAME, 'contacts_email'),
    #     "mobile": (By.NAME, 'contacts_mobile'),
    #     "signatory_name": (By.NAME, 'signatory_name'),
    #     "signatory_designation": (By.NAME, 'signatory_designation'),
    #     "signatory_email": (By.NAME, 'signatory_email'),
    #     "signatory_mobile": (By.NAME, 'signatory_mobile'),
    #     "bank_name": (By.NAME, 'bank_name'),
    #     "branch_name": (By.NAME, 'branch_name'),
    #     "account_name": (By.NAME, 'acccount_name'),
    #     "account_number": (By.NAME, 'account_number'),
    #     "ifsc": (By.NAME, 'ifsc'),
    #     "ngoSubmit": (By.XPATH, '//button[@id="ngoSubmit"]')
    # }
    #
    # # **Methods**
    # def enter_ngo_name(self, name):
    #     self.sel_wrap_obj.enter_text(self.locators['ngo_name'], name)
    #
    # def select_type_of_ngo(self):
    #     self.sel_wrap_obj.click_on_element(self.locators['type_of_ngo'])
    #
    # def check_empelled_partner(self):
    #     self.sel_wrap_obj.click_on_element(self.locators['empelled_partner'])
    #
    # def enter_vendor_code(self, code):
    #     self.sel_wrap_obj.enter_text(self.locators['vendor_code'], code)
    #
    # def select_multiselect(self, values):
    #     """Select multiple NGO types (multi-select)."""
    #     self.sel_wrap_obj.select_multiple_options(self.locators['thematic'], values)
    #
    # def date_picker(self, month_year):
    #     """Select a month in an input[type='month'] field."""
    #
    #     # Locate the input field
    #     date_input = self.wait.until(EC.element_to_be_clickable((By.NAME, "incorporation")))
    #
    #     # Use JavaScript to set the value since onkeydown prevents manual input
    #     self.driver.execute_script("arguments[0].value = arguments[1];", date_input, month_year)
    #
    #     # Trigger change event (important for some frameworks like React)
    #     self.driver.execute_script("arguments[0].dispatchEvent(new Event('change'))", date_input)
    #
    # def enter_registration_details(self, certificate_no, g_reg, a_reg, pan):
    #     self.sel_wrap_obj.enter_text(self.locators['csr_certificate_no'], certificate_no)
    #     self.sel_wrap_obj.enter_text(self.locators['g_registration_number'], g_reg)
    #     self.sel_wrap_obj.enter_text(self.locators['a_registration_number'], a_reg)
    #     self.sel_wrap_obj.enter_text(self.locators['pan'], pan)
    #
    #     # **Method to Select an Option from Dropdown**
    #
    # def select_dropdown(self , g80 , a12):
    #    # self.sel_wrap_obj.select_from_dropdown_by_value(self.locators['incorporation'], incorp)
    #     self.sel_wrap_obj.select_from_dropdown_by_value(self.locators['g80_validity'], g80)
    #     self.sel_wrap_obj.select_from_dropdown_by_value(self.locators['a12_validity'], a12)
    #
    # def enter_contact_details(self, name, designation, email, mobile):
    #     self.sel_wrap_obj.enter_text(self.locators['contact_name'], name)
    #     self.sel_wrap_obj.enter_text(self.locators['designation'], designation)
    #     self.sel_wrap_obj.enter_text(self.locators['email'], email)
    #     self.sel_wrap_obj.enter_text(self.locators['mobile'], mobile)
    #
    # def enter_signatory_details(self, name, designation, email, mobile):
    #     self.sel_wrap_obj.enter_text(self.locators['signatory_name'], name)
    #     self.sel_wrap_obj.enter_text(self.locators['signatory_designation'], designation)
    #     self.sel_wrap_obj.enter_text(self.locators['signatory_email'], email)
    #     self.sel_wrap_obj.enter_text(self.locators['signatory_mobile'], mobile)
    #
    # def enter_bank_details(self, acc_name ,bank, branch, acc_number, ifsc):
    #
    #     self.sel_wrap_obj.enter_text(self.locators['account_name'], acc_name)
    #     self.sel_wrap_obj.enter_text(self.locators['bank_name'], bank)
    #     self.sel_wrap_obj.enter_text(self.locators['branch_name'], branch)
    #     self.sel_wrap_obj.enter_text(self.locators['account_number'], acc_number)
    #     self.sel_wrap_obj.enter_text(self.locators['ifsc'], ifsc)
    #
    #
    # def submit_form(self):
    #     if 'ngoSubmit' not in self.locators:
    #         raise KeyError("Locator for 'submit' not found in self.locators")
    #
    #     wait = WebDriverWait(self.sel_wrap_obj.driver, 10)
    #     submit_button = wait.until(EC.element_to_be_clickable(self.locators['ngoSubmit']))
    #     self.sel_wrap_obj.driver.execute_script("arguments[0].click();", submit_button)





