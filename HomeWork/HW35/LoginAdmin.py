from robot.api.deco import keyword
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from HomeWork.HW35.locators import LoginAdminPageLocators


class LoginAdmin(object):

    @keyword(name="Login Admin")
    def driver(self):
        options = ChromeOptions()
        options.add_argument('--headless')
        wd = webdriver.Chrome(options=options)
        return wd

    @keyword(name="Open Page")
    def open(self):
        url = 'https://192.168.77.43/admin'
        self.driver.get(url)

    @keyword(name="Set Username")
    def set_username(self, username):
        self.driver.find_element(*LoginAdminPageLocators.USERNAME).send_keys(username)

    @keyword(name="Set Password")
    def set_password(self, password):
        self.driver.find_element(*LoginAdminPageLocators.PASSWORD).send_keys(password)

    @keyword(name="Submit")
    def submit(self):
        self.driver.find_element(*LoginAdminPageLocators.SUBMIT).click()
        assert self.driver.title == 'Dashboard'

    @keyword(name="Close")
    def close(self):
        self.driver.quit()
