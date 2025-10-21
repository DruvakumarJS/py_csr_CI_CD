import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Pages.csr_login import LoginPage
from Pages.create_ngo import NgoCreatePage
from Pages.create_project import ProjectPage


@pytest.mark.dependency()
def test_login(_drivers):
    login_object = LoginPage(_drivers)
    login_object.userid_field()
    login_object.password_field()
    login_object.login_button()

@pytest.mark.dependency(depends=["test_login"])
def test_NgoCreate(_drivers):
    _drivers.get("https://csr.netiapps.com/home/CSR/create-NGO")
       #_drivers.get("http://127.0.0.1:8000/home/CSR/create-NGO")

    ngo_page = NgoCreatePage(_drivers)

      # Fill in NGO form

    ngo_object = NgoCreatePage(_drivers)
    ngo_object.enter_ngo_name1()
    ngo_object.select_type_of_ngo1()
    ngo_object.check_empelled_partner()
    ngo_object.enter_vendor_code()
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






