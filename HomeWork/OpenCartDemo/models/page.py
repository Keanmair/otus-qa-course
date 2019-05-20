import pickle
import string

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver import ActionChains


class BasePage:
    """Base class to initialize the base page that will be called from all pages"""

    RU_LETTERS = ''.join([chr(i) for i in range(1040, 1104)])
    SPEC_SIMBOLS = string.punctuation
    DIGITS = string.digits
    ALL_SIMBOLS = RU_LETTERS + SPEC_SIMBOLS + DIGITS

    def __init__(self, driver):
        self.driver = driver

    @property
    def current_url(self):
        return self.driver.current_url

    @property
    def page_width(self):
        return self.driver.execute_script("return Math.max(document.body.scrollWidth,"
                                          " document.body.offsetWidth, "
                                          "document.documentElement.clientWidth, "
                                          "document.documentElement.scrollWidth, "
                                          "document.documentElement.offsetWidth);")

    @property
    def page_height(self):
        return self.driver.execute_script("return Math.max(document.body.scrollHeight, "
                                          "document.body.offsetHeight, "
                                          "document.documentElement.clientHeight, "
                                          "document.documentElement.scrollHeight, "
                                          "document.documentElement.offsetHeight);")

    def find_element(self, locator, element=None):
        """Method for find one element with waiter, if element not found in DOM, from root or from WebElement"""
        # try:
        root = element or self.driver
        return WebDriverWait(root, 3).until(EC.visibility_of_element_located(locator))
        # except (NoSuchElementException, TimeoutException):
        #     return

    def wait_element_presence(self, locator, element=None):

        # try:
        root = element or self.driver
        return WebDriverWait(root, 3).until(EC.presence_of_element_located(locator))
        # except (NoSuchElementException, TimeoutException):
        #     return

    def assert_element_presence(self, locator, element=None):

        # try:
        root = element or self.driver
        try:
            WebDriverWait(root, 3).until(EC.presence_of_element_located(locator))
            return True
        except (NoSuchElementException, TimeoutException):
            return False
        # except (NoSuchElementException, TimeoutException):
        #     return

    def find_elements(self, locator, element=None):
        """Method for finding list of elements, from root or from WebElement"""
        root = element or self.driver
        return root.find_elements(by=locator[0], value=locator[1])

    def open_page(self, url):
        self.driver.get(url)

    def refresh_page(self):
        self.driver.refresh()

    def input_text(self, locator, text):
        self.find_element(locator).clear()
        self.find_element(locator).send_keys(text)

    def drag_and_drop(self, src, dst):
        ActionChains(self.driver).drag_and_drop(src, dst).perform()

    @staticmethod
    def input_text_to_element(element, text):
        element.clear()
        element.send_keys(text)

    def clear_text(self, locator):
        self.find_element(locator).clear()

    def click(self, locator, element=None):
        root = element or self.driver
        self.find_element(locator, root).click()

    def select(self, locator, option):
        selector = Select(self.find_element(locator))
        selector.select_by_visible_text(option)

    def save_cookies(self, file_pkl):
        pickle.dump(self.driver.get_cookie(), open(file_pkl, 'wb'))

    def add_cookies(self, file_pkl):
        self.driver.delete_all_cookies()
        cookies = pickle.load(open(file_pkl, 'rb'))
        for cookie in cookies:
            self.driver.add_cookie(cookie)

    def drag_and_drop_js(self, source, desc):
        """Drag and drop elements with js
        :param source: css_selector (str)
        :param desc: css_selector (str)
        """
        jquery_url = "http://code.jquery.com/jquery-1.12.4.min.js"
        with open('utils/jquery_load_helper.js', 'r') as f:
            load_jquery_js = f.read()
        with open('utils/drag_and_drop_helper.js', 'r') as f:
            drag_and_drop_js = f.read()
        self.driver.execute_async_script(load_jquery_js, jquery_url)
        self.driver.execute_script(
            drag_and_drop_js + "$('%s').simulateDragDrop({ dropTarget: '%s' });" % (source, desc))

    @staticmethod
    def convert_timer_to_sec(timer):
        """Convert default system timer to seconds
        :param timer: str, e.g. '1:02:30:15'
        :return: time in seconds (int)
        """
        a = [int(i) for i in timer.split(':')]
        b = [86400, 3600, 60, 1]
        return sum(map(lambda x, y: x * y, a, b))

    def get_title_page(self):
        return self.find_element(self.locators.TITLE).text
