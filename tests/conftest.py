import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def driver():
    """Setup Chrome driver for entire test session"""
    opt = webdriver.ChromeOptions()
    opt.add_experimental_option("detach", True)
    opt.add_argument("--disable-notifications")

    driver = webdriver.Chrome(options=opt)
    driver.get("https://csr.netiapps.com/login")
    driver.maximize_window()
    driver.implicitly_wait(20)

    yield driver
    driver.quit()


# ---------------- HTML Report Customization ---------------- #

def pytest_html_report_title(report):
    report.title = "CSR Automation Test Report"

def pytest_html_results_summary(prefix, summary, postfix):
    """Add custom metadata to report summary"""
    prefix.extend([f"Project: CSR Automation",
                   f"Tester: Druva",
                   f"Environment: Staging"])


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Attach test description to HTML report"""
    outcome = yield
    report = outcome.get_result()
    if report.when == "call":
        report.description = str(item.function.__doc__)


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    """Add Description column to HTML report"""
    cells.insert(2, '<th>Description</th>')
    cells.pop()


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    """Display test description in HTML report"""
    cells.insert(2, f"<td>{report.description}</td>")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_logreport(report):
    """Ensure logs are captured even when tests pass"""
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.passed:
        report.sections.append(("Captured Log", "Test executed successfully."))
