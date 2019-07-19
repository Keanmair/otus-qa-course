from selenium import webdriver
import pytest


class Browser:
    def __init__(self, browser):

        if browser == 'Chrome_local':
            self.wd = webdriver.Chrome()

        elif browser == "Chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            self.wd = webdriver.Remote(command_executor="http://localhost:4444/wd/hub",
                                       desired_capabilities=options.to_capabilities())

        elif browser == 'Firefox_local':
            self.wd = webdriver.Firefox()


@pytest.fixture(scope="session")
def driver(browser):
    driver = Browser(browser).wd
    driver.maximize_window()
    driver.implicitly_wait(15)
    yield driver
    driver.quit()


def test_hub(driver):
    driver.get("https://yandex.ru/")
    print(driver.title)
    driver.save_screenshot('grid_screen.png')
    assert driver.title == 'Яндекс'
