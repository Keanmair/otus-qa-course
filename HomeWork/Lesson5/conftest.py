import pytest
from selenium import webdriver
import logging

# __logger = logging.getLogger('Lololo')
# __logger.setLevel('INFO')


def __str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise TypeError('Boolean value expected.')


def chrome_browser():
    options = webdriver.ChromeOptions()
    options.headless = True
    chromedriver = "/home/korneev/Drivers/chromedriver"
    driver = webdriver.Chrome(executable_path=chromedriver, options=options)
    driver.maximize_window()
    return driver


def firefox_browser():
    options = webdriver.FirefoxOptions()
    options.headless = True
    firefoxdriver = "/home/korneev/Drivers/geckodriver"
    driver = webdriver.Firefox(executable_path=firefoxdriver, options=options)
    driver.maximize_window()
    return driver


def pytest_addoption(parser):
    parser.addoption("--brw", action="store", default="c", help="My option: c for Chrome, f for Firefox")
    parser.addoption("--url", action="store", type=__str2bool, default=False, help="My option: True or False")


@pytest.fixture
def brw(request):
    if request.config.getoption("--url"):
        print("\nBase URL: http://192.168.77.43/opencart/")
        # __logger.info("http://192.168.77.43/opencart/")

    if request.config.getoption("--brw") == "f":
        drv = firefox_browser()
    if request.config.getoption("--brw") == "c":
        drv = chrome_browser()
    request.addfinalizer(drv.quit)
    return drv

# baseUrl == "http://192.168.77.43/opencart/"
