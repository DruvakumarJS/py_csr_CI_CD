import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pytest_html import extras  # For report logging

from Pages.csr_login import LoginPage
from Pages.create_ngo import NgoCreatePage
from Pages.create_project import ProjectPage

def log_to_report(request, message):
    """Attach custom log messages into pytest-html report"""
    if hasattr(request.node, "add_report_section"):
        request.node.add_report_section("call", "message", message)
    print(message)  # still prints to console

@pytest.mark.dependency()
def test_login(_drivers, request):
    login_object = LoginPage(_drivers)

    username = login_object.userid_field()
    password = login_object.password_field()

    # capture messages dynamically
    log_to_report(request, f"Entered Username: {username}")
    log_to_report(request, f"Entered Password: {password}")

    login_object.login_button()



@pytest.mark.dependency(depends=["test_login"])
def test_NgoCreate(_drivers,request):
    _drivers.get("https://csr.netiapps.com/home/CSR/create-NGO")

    ngo_page = NgoCreatePage(_drivers)

      # Fill in NGO form

    # ngo_object.enter_ngo_name1()
    # ngo_object.select_type_of_ngo1()
    # ngo_object.check_empelled_partner()
    # ngo_object.enter_vendor_code()

    ngo_name = ngo_page.enter_ngo_name1()  # make sure it returns the entered value
    ngo_type = ngo_page.select_type_of_ngo1()
    empelled = ngo_page.check_empelled_partner()
    vendor_code = ngo_page.enter_vendor_code()

    # Attach messages to report
    log_to_report(request, f"NGO Name Entered: {ngo_name}")
    log_to_report(request, f"NGO Type Selected: {ngo_type}")
    log_to_report(request, f"Empelled Partner Checked: {empelled}")
    log_to_report(request, f"Vendor Code Entered: {vendor_code}")


    ngo_page.select_multiselect()
    ngo_page.date_picker()
    ngo_page.enter_registration_details()
    ngo_page.select_dropdown()
    ngo_page.enter_contact_details()

    time.sleep(2)

    ngo_page.submit_form()

       # Wait for Swal alert to appear
    swal_locator = (By.CLASS_NAME, "swal2-popup")
    WebDriverWait(ngo_page.driver, 10).until(EC.visibility_of_element_located(swal_locator))
    time.sleep(3)
        # Get Swal message
    ok_button_locator = (By.CLASS_NAME, "swal2-confirm")
    WebDriverWait(ngo_page.driver, 10).until(EC.element_to_be_clickable(ok_button_locator)).click()

    time.sleep(3)

# @pytest.mark.dependency(depends=["test_NgoCreate"])
# def test_ProjectCreate(_drivers):
#     _drivers.get("https://csr.netiapps.com/home/CSR/project-onboarding/create-project/new")
#    # _drivers.get("http://127.0.0.1:8000/home/CSR/project-onboarding/create-project/new")
#
#     project_page = ProjectPage(_drivers)
#     project_page.fill_project_details()
#     time.sleep(10)






