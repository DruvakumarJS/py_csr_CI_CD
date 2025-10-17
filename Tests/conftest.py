from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pytest
from selenium import webdriver

# Opening the browser
opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach", True)
opt.add_argument("--disable-notifications")


# Opening the website
@pytest.fixture(scope="session")
def _drivers():
    driver = webdriver.Chrome(options=opt)
    driver.get("https://csr.netiapps.com/login")
   # driver.get("http://127.0.0.1:8000/login")
    driver.maximize_window()
    driver.implicitly_wait(20)
    yield driver
    driver.quit()

