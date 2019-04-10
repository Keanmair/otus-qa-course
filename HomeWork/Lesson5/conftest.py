import pytest
from selenium import webdriver
import logging

# __logger = logging.getLogger('Lololo')
# __logger.setLevel('INFO')

baseUrl = "http://192.168.77.43/opencart/"


# def __str2bool(v):
#     if v.lower() in ('yes', 'true', 't', 'y', '1'):
#         return True
#     elif v.lower() in ('no', 'false', 'f', 'n', '0'):
#         return False
#     else:
#         raise TypeError('Boolean value expected.')


def chrome_browser(url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.headless = True
    # chrome_driver = "/home/korneev/Drivers/chromedriver"
    driver = webdriver.Chrome(options=chrome_options) #executable_path=chrome_driver,
    driver.maximize_window()
    driver.get(url)
    return driver


def firefox_browser(url):
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.headless = True
    # firefox_driver = "/home/korneev/Drivers/geckodriver"
    driver = webdriver.Firefox(options=firefox_options) #executable_path=firefox_driver,
    driver.maximize_window()
    driver.get(url)
    return driver


def pytest_addoption(parser):
    parser.addoption("--brw", action="store", default="c", help="Browser option: c for Chrome, f for Firefox")
    parser.addoption("--url", action="store", default=baseUrl, help="URL option: input url for test")


@pytest.fixture
def brw(request):
    print("\n"+request.config.getoption("--url"))
    # __logger.info("http://192.168.77.43/opencart/")

    if request.config.getoption("--brw") == "f":
        drv = firefox_browser(request.config.getoption("--url"))
    if request.config.getoption("--brw") == "c":
        drv = chrome_browser(request.config.getoption("--url"))
    request.addfinalizer(drv.quit)
    return drv

