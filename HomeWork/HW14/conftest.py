import pytest
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
import logging
import os
import platform
import sqlite3
from datetime import datetime


class Handler(AbstractEventListener):
    def __init__(self):
        self.last_elem = None
        self.log = ''.join((os.path.abspath(os.curdir), "/screenshots/"))
        if not os.path.exists(self.log):
            os.makedirs(os.path.abspath(os.curdir))
        self.conn = sqlite3.connect(''.join((self.log, 'log.db')))
        self.createtable()

    def createtable(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS Logs (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                                            date TEXT, 
                                                            before_find TEXT,
                                                            after_find TEXT,
                                                            exeption TEXT);''')
        cursor.close()

    def write_log(self, string):
        cursor = self.conn.cursor()
        print(string)
        cursor.execute(string)
        cursor.close()

    def before_find(self, by, value, driver):
        logging.log(level=10, msg="LOG")
        val = value.replace('"', "'")
        self.last_elem = datetime.timestamp(datetime.now())
        elem = 'INSERT INTO Logs (date, before_find) VALUES ("%s", "%s");' % (self.last_elem, val)
        self.write_log(elem)

    def after_find(self, by, value, driver):
        print(by, value, "found")
        elem = 'UPDATE Logs SET after_find="%s" WHERE date = "%s";' % ('found', self.last_elem)
        self.write_log(elem)

    def on_exception(self, exception, driver):
        elem = 'UPDATE Logs SET exeption="%s" WHERE date = "%s";' % (exception, self.last_elem)
        self.write_log(elem)

    def before_quit(self, driver):
        print("QUIT!")
        self.conn.commit()
        self.conn.close()


baseUrl = "http://192.168.77.43/opencart/admin/"


def pytest_addoption(parser):
    parser.addoption("--brw", action="store", default="c", help="Browser option: c for Chrome, f for Firefox")
    parser.addoption("--url", action="store", default=baseUrl, help="URL option: input url for test")


@pytest.fixture(scope="session", autouse=True)
def driver(request):
    wd = None
    def_opt = ["--start-halfscreen"]  # ["--headless"]
    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        options = webdriver.ChromeOptions()
        bin = "/usr/local/bin/chromedriver"
        for argg in def_opt:
            options.add_argument(argg)
        wd = EventFiringWebDriver(webdriver.Chrome(executable_path=bin, chrome_options=options), Handler())
    else:
        options = webdriver.FirefoxOptions()
        bin = "/usr/local/bin/geckodriver"
        for argg in def_opt:
            options.add_argument(argg)
        wd = EventFiringWebDriver(webdriver.Firefox(executable_path=bin, firefox_options=options), Handler())
    yield wd
    wd.quit()


@pytest.mark.usefixtures("environment_info")
@pytest.fixture(scope='session', autouse=True)
def configure_html_report_env(request, environment_info):
    request.config._metadata.update(
        {"browser": request.config.getoption("--browser"),
         "address": request.config.getoption("--url"),
         "os platform": environment_info[0],
         "os": environment_info[1],
         "python v": environment_info[2]})
    yield


@pytest.mark.usefixtures("environment_info")
@pytest.fixture(scope='session', autouse=True)
def extra_json_environment(request, environment_info):
    request.config._json_environment.append(("os platform", environment_info[0]))
    request.config._json_environment.append(("python v", environment_info[2]))


@pytest.fixture(scope="session")
def environment_info():
    os_platform = platform.platform()
    dist = platform.system()
    python = platform.python_version()
    return os_platform, dist, python
