import time

from selenium.webdriver.common.by import By

from Data.Reading_excel import project_locators

from Library.selenium_wrapper import SeleniumWrapper
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

locators = project_locators()  # Ensure correct path

class ProjectPage:
    def __init__(self, driver):
        self.driver = driver
        self.sel_wrap_obj = SeleniumWrapper(self.driver)
        self.wait = WebDriverWait(self.driver, 10)

        #common function
    def enter_text_value(self, key):
        """Reusable function to enter text for any locator key."""
        self.sel_wrap_obj.enter_text((locators[key][0], locators[key][1]), locators[key][2])
        time.sleep(2)

    def select_dropdown_value(self, key):
        """Reusable function to select dropdown value for any locator key."""
        self.sel_wrap_obj.select_from_dropdown_by_value((locators[key][0], locators[key][1]),
                                                        locators[key][2])
        time.sleep(2)

    def select_multiselect_value(self, key):
        """Reusable function to select dropdown value for any locator key."""
        self.sel_wrap_obj.select_from_multiselect_value((locators[key][0], locators[key][1]),
                                                        locators[key][2])
        time.sleep(2)

    def date_picker(self, key):
        """Set a date for input fields of type 'date' using JavaScript."""

        date_input = self.wait.until(EC.presence_of_element_located((locators[key][0], locators[key][1])))
        date_value = "2025-03-03"  # Format: YYYY-MM-DD from Excel

        # ✅ Set the date and force trigger change event
        self.driver.execute_script("""
            arguments[0].removeAttribute('readonly');  // Remove 'readonly' if exists
            arguments[0].setAttribute('value', arguments[1]); // Set the date
            arguments[0].dispatchEvent(new Event('input', { bubbles: true })); // Trigger event
            arguments[0].dispatchEvent(new Event('change', { bubbles: true })); // Ensure form detects it
        """, date_input, date_value)

        time.sleep(2)

    def select_autocomplete_value(self, key):
        """Selects the first item from an autocomplete dropdown after entering a value."""
        try:
            print(f"🔍 Locating input field for {key}...")
            input_field = self.wait.until(EC.element_to_be_clickable((locators[key][0], locators[key][1])))
            input_field.clear()

            input_value = locators[key][2]
            print(f"📝 Entering value: {input_value} in {key}")
            input_field.send_keys(input_value)
            time.sleep(2)  # Allow dropdown to populate

            # Find dropdown options
            option_xpath = "//ul[contains(@class, 'ui-autocomplete')]//li[contains(@class, 'ui-menu-item')]/div"
            self.wait.until(EC.presence_of_element_located((By.XPATH, option_xpath)))

            dropdown_options = self.driver.find_elements(By.XPATH, option_xpath)
            print(f"📋 Found {len(dropdown_options)} options in dropdown.")

            if dropdown_options:
                print(f"✅ Clicking first option: {dropdown_options[0].text}")
                self.driver.execute_script("arguments[0].scrollIntoView();", dropdown_options[0])
                self.driver.execute_script("arguments[0].click();", dropdown_options[0])  # Using JS click

                time.sleep(1)  # Allow UI update
                print(f"✅ Successfully selected first option for {key}")
            else:
                print(f"❌ No options found in dropdown for {key}")

        except Exception as e:
            print(f"❌ Error in select_autocomplete_value: {str(e)}")

        # beneficiary

    def select_multiselect_benef_value(self, key):
        """Reusable function to select dropdown value for any locator key."""
        self.sel_wrap_obj.select_from_multiselect_benif_value((locators[key][0], locators[key][1]),
                                                        locators[key][2])
        time.sleep(2)

    def submit_project(self, key):
        """Reusable function to enter text for any locator key."""
        self.sel_wrap_obj.submit((locators[key][0], locators[key][1]))
        time.sleep(2)

    def fill_project_details(self):
        self.enter_text_value("title")  # Fetches from Excel
        self.select_dropdown_value("implementation_type")
        self.select_dropdown_value("ngo_id")
        self.enter_text_value("referred_by")
        self.date_picker("proposal_received_date")
        self.select_dropdown_value("proposal_received_at")
        self.select_dropdown_value("primary_thematic_area")
        self.select_dropdown_value("secondary_thematic_area")
        self.enter_text_value("project_location")
        self.select_dropdown_value("year_of_execution")
        self.select_dropdown_value("region_of_excution")
        self.select_dropdown_value("gl_locations")
        self.select_autocomplete_value("branch_code")
        self.select_multiselect_value("csr_district_type")
        self.enter_text_value("project_duration")
        self.select_multiselect_benef_value("beneficiaries")
        self.enter_text_value("project_note")

        self.submit_project("project_save")










