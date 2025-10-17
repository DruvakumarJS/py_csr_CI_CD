import time
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class SeleniumWrapper:
    def __init__(self, driver):
        """Initialize the Selenium Wrapper with a WebDriver instance."""
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)  # ✅ Fix: Initialize WebDriverWait

    def select_dropdown1(self, logical_name, data):
        """Select an option from a dropdown by visible text."""
        dropdown = Select(self.driver.find_element(*logical_name))
        dropdown.select_by_visible_text(data)

    def enter_text(self, logical_name, data):
        """Enter text into an input field."""
        self.driver.find_element(*logical_name).send_keys(data)

    def click_on_element(self, logical_name):
        """Click on an element."""
        self.driver.find_element(*logical_name).click()

    def find_element(self, by, locator):
        """Find an element with explicit wait."""
        return self.wait.until(EC.presence_of_element_located((by, locator)))

    def select_multiple_options(self, locator, values):
        """Select multiple options from a multi-select dropdown."""
        dropdown = Select(self.get_element(locator))

        if not dropdown.is_multiple:
            raise Exception("Dropdown does not support multiple selection!")

        for value in values:
            try:
                dropdown.select_by_visible_text(value)  # More reliable
            except:
                print(f"Option '{value}' not found!")

       # print(f"Selected: {values}")


    def get_element(self, locator):
        """Wait for the element to be present and return it."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def select_from_dropdown_by_value(self, locator, value):
        """Select an option from a dropdown using its value."""
        dropdown = Select(self.get_element(locator))
        dropdown.select_by_visible_text(value)

    def select_from_multiselect_value(self, locator, values):
        """Select multiple values from a multi-select dropdown."""
        print(f"✅ locator: {locator}")
        print(f"✅ values: {values}")
        try:
            dropdown = Select(self.get_element(locator))

            # 🔹 Ensure values are split correctly and remove any extra spaces
            if isinstance(values, str):
                values = [val.strip() for val in values.split(",")]  # Trim spaces around values

            for value in values:
                try:
                    dropdown.select_by_visible_text(value)
                    print(f"✅ Selected: {value}")
                except:
                    print(f"❌ Option '{value}' not found in dropdown!")

        except Exception as e:
            print(f"❌ Error in select_from_multiselect_value: {str(e)}")


    # def select_from_multiselect_benif_value(self, locator, values):
    #     """Select multiple values from a multi-select dropdown."""
    #     print(f"✅ locator: {locator}")
    #     print(f"✅ values: {values}")
    #     try:
    #         dropdown = Select(self.get_element(locator))
    #
    #         # 🔹 Ensure values are split correctly and remove any extra spaces
    #         if isinstance(values, str):
    #             values = [val.strip() for val in values.split(",")]  # Trim spaces around values
    #
    #         for value in values:
    #             try:
    #                 dropdown.select_by_visible_text(value)
    #                 print(f"✅ Selected: {value}")
    #             except:
    #                 print(f"❌ Option '{value}' not found in dropdown!")
    #
    #     except Exception as e:
    #         print(f"❌ Error in select_from_multiselect_value: {str(e)}")

    from selenium.webdriver.support.ui import Select, WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By

    def select_from_multiselect_benif_value(self, locator, values):
        try:
            dropdown = Select(self.get_element(locator))

            if isinstance(values, str):
                values = [val.strip() for val in values.split(",")]

            for value in values:
                try:
                    dropdown.select_by_visible_text(value)
                    print(f"✅ Selected: {value}")
                except Exception as e:
                    print(f"❌ Option '{value}' not found: {e}")

            # Wait a little extra before filling
            self.driver.implicitly_wait(2)

            # Debug: List all inputs
            print("🔍 Available inputs after selection:")
            inputs = self.driver.find_elements(By.TAG_NAME, "input")
            for i in inputs:
                print(" 👉", i.get_attribute("id"))

            # Fill the inputs
            for i in range(len(values)):
                input_id = f"proposed_benificiary_id_{i}"  # updated to match real ID
                try:
                    WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.ID, input_id))
                    )
                    elem = self.driver.find_element(By.ID, input_id)
                    elem.clear()
                    elem.send_keys(f"Test Value {100*(i+1)}")
                    print(f"📝 Filled {input_id} with 'Test Value {i}'")
                except Exception as e:
                    print(f"❌ Could not fill {input_id}: {repr(e)}")

        except Exception as e:
            print(f"❌ Error in select_from_multiselect_benif_value: {repr(e)}")

    def submit(self, param):
        print(f"✅ param: {param}")
        self.driver.find_element(*param).click()


