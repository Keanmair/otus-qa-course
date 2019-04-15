from HomeWork.Lesson6.models.locator import LoginPageLocators
from HomeWork.Lesson6.models.page import BasePage


class LoginPage(BasePage):

    def set_username(self, username):
        self.driver.find_element(*LoginPageLocators.Username).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(*LoginPageLocators.Password).send_keys(password)

    def login_button(self):
        self.find_element(LoginPageLocators.LoginButton).click()

    def clear_login(self):
        self.clear_text(self.driver.find_element(*LoginPageLocators.Username))

    def clear_password(self):
        self.clear_text(self.driver.find_element(*LoginPageLocators.Password))
