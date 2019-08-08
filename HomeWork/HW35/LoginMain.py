from robot.api.deco import keyword
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from HomeWork.HW35.locators import LoginMainPageLocators


class LoginMain(object):

    @keyword(name="Login Main")
    def driver(self):
        options = ChromeOptions()
        options.add_argument('--headless')
        wd = webdriver.Chrome(options=options)
        return wd

    @keyword(name="Open Page")
    def open(self):
        url = 'https://192.168.77.43/index.php?route=account/login'
        self.driver.get(url)

    @keyword(name="Set Email")
    def set_email(self, email):
        self.driver.find_element(*LoginMainPageLocators.EMAIL).send_keys(email)

    @keyword(name="Set Password")
    def set_password(self, password):
        self.driver.find_element(*LoginMainPageLocators.PASSWORD).send_keys(password)

    @keyword(name="Submit")
    def login(self):
        self.driver.find_element(*LoginMainPageLocators.SUBMIT).click()
        assert self.driver.title == 'My Account'

    @keyword(name="Close")
    def close(self):
        self.driver.quit()
