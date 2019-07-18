import pytest
from selenium import webdriver
import platform
import subprocess


@pytest.fixture(scope="module")
def init_webdriver():
    options = webdriver.ChromeOptions()

    driver = webdriver.Remote(command_executor="http://192.168.77.43:4444/wd/hub",
                              desired_capabilities=options.to_capabilities())
    driver.get("https://www.google.com/")
    print(driver.title)
    yield driver
    driver.quit()


def test_ping():
    assert ping("www.google.com") == True


def test_title(init_webdriver):
    print("test start")
    assert init_webdriver.title == "Google"
    print("test end")


def ping(host):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '4', host]
    return subprocess.call(command) == 0


print('start')
print(ping('www.google.com'))
print('end')
