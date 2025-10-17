import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def _drivers():
    opt = webdriver.ChromeOptions()
    opt.add_experimental_option("detach", True)
    opt.add_argument("--disable-notifications")

    driver = webdriver.Chrome(options=opt)
    driver.get("https://csr.netiapps.com/login")
    driver.maximize_window()
    driver.implicitly_wait(20)

    yield driver
    driver.quit()
