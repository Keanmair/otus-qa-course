import pytest
from selenium import webdriver
from selenium.webdriver.support.events import AbstractEventListener
import logging
import sqlite3
from datetime import datetime

from HomeWork.HW20.pages import AdminPage, LoginPage, ProductPage


def log():
    log_timestamp = str(datetime.datetime.now())[0:-4].replace('-', '.').replace(' ', '_').replace(':', '.')
    logger = logging.getLogger("WebTestApp")
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler(log_timestamp + "_logging.log")
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    logger.info("-----------------------------")
    logger.info("Program started")


class MyListener(AbstractEventListener):

    def __init__(self):
        self.log_timestamp = str(datetime.datetime.now())[0:-4].replace('-', '.').replace(' ', '_').replace(':', '.')
        self.log_filename = self.log_timestamp + '_file.log'
        self.logfile = open(self.log_filename, 'w')
        self.logdb_filename = (self.log_timestamp + '_log.sqlite3')
        self.logdb = sqlite3.connect(self.logdb_filename)
        self.cursor = self.logdb.cursor()
        self.cursor.execute("CREATE TABLE log (timestamp a_string, message a_string)")
        self.logdb.commit()
        self.logdb.close()
        log()
        self.logger = logging.getLogger("WebTestApp")

    def _write_log_(self, entry):
        self.logfile.write(entry + '\n')

    def _write_log_db_(self, entry):
        self.logdb = sqlite3.connect(self.logdb_filename)
        self.cursor = self.logdb.cursor()
        timestamp = str(datetime.datetime.now())[0:-4].replace('-', '.').replace(' ', '_').replace(':', '.')
        self.cursor.execute("INSERT INTO log VALUES ('{}', '{}')".format(timestamp, entry))
        self.logdb.commit()
        self.logdb.close()

    def before_navigate_to(self, url, driver):
        print("Before navigate to {}".format(url))
        self._write_log_("Before navigate to {}".format(url))
        self._write_log_db_("Before navigate to {}".format(url))
        self.logger.info("Before navigate to {}".format(url))

    def after_navigate_to(self, url, driver):
        print("After navigate to {}".format(url))
        self._write_log_("After navigate to {}".format(url))
        self._write_log_db_("After navigate to {}".format(url))
        self.logger.info("After navigate to {}".format(url))

    def before_find(self, by, value, driver):
        print("Before find {} {}".format(by, value))
        self._write_log_("Before find {} {}".format(by, value))
        value = value.replace("'", '"')
        self._write_log_db_('Before find {} {}'.format(by, value))
        self.logger.info("Before find {} {}".format(by, value))

    def after_find(self, by, value, driver):
        print("After find {} {}".format(by, value))
        self._write_log_("After find {} {}".format(by, value))
        value = value.replace("'", '"')
        self._write_log_db_('After find {} {}'.format(by, value))
        self.logger.info("After find {} {}".format(by, value))

    def before_click(self, element, driver):
        print("Before click {}".format(element))
        self._write_log_("Before click {}".format(element.get_attribute("class")))
        self._write_log_db_("Before click {}".format(element.get_attribute("class")))
        self.logger.info("Before click {}".format(element.get_attribute("class")))

    def after_click(self, element, driver):
        print("After click")
        self._write_log_("After click")
        self._write_log_db_("After click")
        self.logger.info("After click")

    def before_execute_script(self, script, driver):
        print("Before execute script {}".format(script))
        self._write_log_("Before execute script {}".format(script))
        self._write_log_db_("Before execute script {}".format(script))
        self.logger.info("Before execute script {}".format(script))

    def after_execute_script(self, script, driver):
        print("After execute script {}".format(script))
        self._write_log_("After execute script {}".format(script))
        self._write_log_db_("After execute script {}".format(script))
        self.logger.info("After execute script {}".format(script))

    def before_close(self, driver):
        print("Before close")
        self._write_log_("Before close")
        self._write_log_db_("Before close")
        self.logger.info("Before close")

    def after_close(self, driver):
        print("After close")
        self._write_log_("After close")
        self._write_log_db_("After close")
        self.logger.info("After close")

    def before_quit(self, driver):
        print("Before quit")
        self._write_log_("Before quit")
        self._write_log_db_("Before quit")
        self.logger.info("Before quit")

    def after_quit(self, driver):
        print("After quit")
        self._write_log_("After quit")
        self._write_log_db_("After quit")
        self.logger.info("After quit")

    def on_exception(self, exception, driver):
        screenshot_timestamp = str(datetime.datetime.now())[0:-4].replace('-', '.').replace(' ', '_').replace(':', '.')
        screenshot_filename = screenshot_timestamp + 'exception_screenshot.png'
        print("On exception {}".format(exception))
        self._write_log_("On exception {}".format(exception))
        self._write_log_db_("On exception {}".format(exception))
        driver.save_screenshot('screenshots/' + screenshot_filename)


baseUrl = "http://192.168.77.43/opencart/admin/"
# baseUrl = "http://127.0.0.1/"


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
    parser.addoption("--wait_time", action="store", default=10, help="wait time option")
    parser.addoption("--window_option", action="store", default="window", help="window option")
    parser.addoption("--waits", action="store", default="no_wait", help="wait option")


@pytest.fixture
def cmdopt_browser(request):
    return request.config.getoption("--brw")


@pytest.fixture
def cmdopt_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def cmdopt_window(request):
    return request.config.getoption("--window_option")


@pytest.fixture
def cmdopt_waits(request):
    return request.config.getoption("--waits")


@pytest.fixture
def cmdopt_wait_time(request):
    return request.config.getoption("--wait_time")


@pytest.fixture(scope="session", autouse=True)
def get_driver(request):
    print("\n" + request.config.getoption("--url"))
    if request.config.getoption("--brw") == "f":
        drv = firefox_browser(request.config.getoption("--url"))
    if request.config.getoption("--brw") == "c":
        drv = chrome_browser(request.config.getoption("--url"))
    request.addfinalizer(drv.quit)
    return drv


@pytest.fixture
def add_waits(get_driver, cmdopt_wait_time):
    driver = get_driver
    if cmdopt_waits == "waits":
        driver.implicitly_wait(cmdopt_wait_time)
    else:
        pass
    return driver


@pytest.fixture
def login_param():
    login = "admin"
    password = "admin"
    return login, password


@pytest.fixture()
def product_dataset():
    product_name = 'Phone_1'
    product_meta_tag_title = 'Phone_1'
    product_model = 'Phone_1'
    return product_name, product_meta_tag_title, product_model


@pytest.fixture()
def product_dataset_more():
    product_name = 'Phone_2'
    product_meta_tag_title = 'Phone_2'
    product_model = 'Phone_2'
    return product_name, product_meta_tag_title, product_model


@pytest.fixture
def login(add_waits, cmdopt_url, login_param):
    login_page = LoginPage(add_waits, cmdopt_url)
    login_page.navigate()
    login, password = login_param
    login_page.login(login, password)
    login_page.close_modal_window()
    return login_page.get_url()


@pytest.fixture
def login_negative(get_driver, cmdopt_url):
    login_page = LoginPage(get_driver, cmdopt_url)
    login_page.navigate()
    login_page.login("admin", "admin1")
    current_result = login_page.get_alert_loginpage()
    expected_result = "No match for Username and/or Password."
    return expected_result, current_result


@pytest.fixture
def go_to_product_page(add_waits, login):
    admin_page = AdminPage(add_waits, login)
    admin_page.navigate()
    admin_page.close_modal_window()
    admin_page.choose_catalog()
    admin_page.choose_product()
    return admin_page.get_url()


@pytest.fixture
def add_product(add_waits, go_to_product_page, product_dataset):
    product_page = ProductPage(add_waits, go_to_product_page)
    product_page.navigate()
    product_name, product_meta_tag_title, product_model = product_dataset
    product_page.add_product(product_name, product_meta_tag_title, product_model)
    current_result = product_page.get_alert()
    expected_result = "Success: You have modified products!"
    return expected_result, current_result


@pytest.fixture
def modify_product(add_waits, go_to_product_page, product_dataset_more):
    product_page = ProductPage(add_waits, go_to_product_page)
    product_page.navigate()
    product_name, product_meta_tag_title, product_model = product_dataset_more
    product_page.add_product(product_name, product_meta_tag_title, product_model)
    product_page.modify_product()
    current_result = product_page.get_alert()
    expected_result = "Success: You have modified products!"
    return expected_result, current_result


@pytest.fixture
def delete_product(add_waits, go_to_product_page, product_dataset_more):
    product_page = ProductPage(add_waits, go_to_product_page)
    product_page.navigate()
    product_name, product_meta_tag_title, product_model = product_dataset_more
    product_page.add_product(product_name, product_meta_tag_title, product_model)
    product_page.delete_product()
    current_result = product_page.get_alert()
    expected_result = "Success: You have modified products!"
    return expected_result, current_result
