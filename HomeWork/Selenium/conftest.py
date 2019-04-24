import pytest
from selenium import webdriver


baseUrl = "http://192.168.77.43/opencart/admin/"


def chrome_browser(url):
    chrome_options = webdriver.ChromeOptions()
    capabilities = webdriver.DesiredCapabilities.CHROME.copy()
    capabilities['timeouts'] = {'implicit': 3000, 'pageLoad': 3000, 'script': 30000}
    chrome_options.headless = False
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get(url)
    return driver


def firefox_browser(url):
    firefox_options = webdriver.FirefoxOptions()
    capabilities = webdriver.DesiredCapabilities.FIREFOX.copy()
    capabilities['timeouts'] = {'implicit': 3000, 'pageLoad': 3000, 'script': 30000}
    firefox_options.headless = True
    driver = webdriver.Firefox(options=firefox_options)
    driver.maximize_window()
    driver.get(url)
    return driver


def pytest_addoption(parser):
    parser.addoption("--brw", action="store", default="c", help="Browser option: c for Chrome, f for Firefox")
    parser.addoption("--url", action="store", default=baseUrl, help="URL option: input url for test")


@pytest.fixture(scope="session", autouse=True)
def brw(request):
    print("\n"+request.config.getoption("--url"))
    if request.config.getoption("--brw") == "f":
        drv = firefox_browser(request.config.getoption("--url"))
    if request.config.getoption("--brw") == "c":
        drv = chrome_browser(request.config.getoption("--url"))
    request.addfinalizer(drv.quit)
    return drv

