from selenium import webdriver
from selenium.webdriver import ActionChains

from HomeWork.OpenCartDemo.conftest import brw
from HomeWork.OpenCartDemo.models.locator import LoginPageLocators, DashboardLocators, DragNDrop
from HomeWork.OpenCartDemo.models.page import BasePage


class LoginPage(BasePage):

    def set_username(self, username):
        self.find_element(LoginPageLocators.Username).send_keys(username)

    def set_password(self, password):
        self.find_element(LoginPageLocators.Password).send_keys(password)

    def login_button(self):
        self.find_element(LoginPageLocators.LoginButton).click()


class Dashboard(BasePage):

    def menu_button(self):
        self.find_element(DashboardLocators.Menu).click()

    def constructor_button(self):
        self.find_element(DashboardLocators.Constructor).click()


class Drag(BasePage):
    def drag_n_drop(self):
        source = self.find_element(DragNDrop.SourceElem)
        dest = self.find_element(DragNDrop.DestElem)
        self.drag_and_drop(source, dest)

    def succsefull_drag(self, text):
        current_text = self.find_element(DragNDrop.SuccsesDrag).text
        if text in current_text:
            return True
        else:
            return False
