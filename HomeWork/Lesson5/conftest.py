import pytest
from selenium import webdriver
from webdrivermanager import ChromeDriverManager


@pytest.fixture
def chrome_browser(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--start-maximized")
    chromedriver = "/home/korneev/Drivers/chromedriver"
    # wd = webdriver.Chrome(ChromeDriverManager().download_and_install(), options=options)
    driver = webdriver.Chrome(executable_path=chromedriver)
    # wd.implicitly_wait()
    # wd.set_page_load_timeout()
    driver.maximize_window()
    request.addfinalizer(driver.quit)
    return driver

@pytest.fixture
def firefox_browser(request):
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    options.add_argument("--start-maximized")
    firefoxdriver = "/home/korneev/Drivers/geckodriver"
    driver = webdriver.Firefox(executable_path=firefoxdriver)
    driver.maximize_window()
    request.addfinalizer(driver.quit)
    return driver

def test_chrome(chrome_browser):
    chrome_browser.get("http://192.168.77.43/opencart//")
    assert chrome_browser.find_element_by_class_name('col-sm-4').text == 'Your Store'

def test_firefox(firefox_browser):
    firefox_browser.get(("http://192.168.77.43/opencart//"))
    assert chrome_browser.find_element_by_class_name('col-sm-4').text == 'Your Store'