from HomeWork.Selenium.models.locator import LoginPageLocators, ForgottenPasswordLocators, ProductsPageLocators, DashboardLocators
from HomeWork.Selenium.models.page import BasePage


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

    def forgotten_password_button(self):
        self.find_element(LoginPageLocators.ForgottenPassword).click()


class ForgottenPage(BasePage):

    def set_email(self, email):
        self.driver.find_element(*ForgottenPasswordLocators.Email).send_keys(email)

    def reset_button(self):
        self.find_element(ForgottenPasswordLocators.ResetButton).click()

    def back_button(self):
        self.find_element(ForgottenPasswordLocators.BackButton).click()


class Dashboard(BasePage):

    def menu_catalog_button(self):
        self.find_element(DashboardLocators.MenuCatalog).click()

    def categories_button(self):
        self.find_element(DashboardLocators.Categories).click()


class ProductsPage(BasePage):

    def add_product_button(self):
        self.find_element(ProductsPageLocators.AddProductButton).click()

    def delete_product_button(self):
        self.find_element(ProductsPageLocators.DeleteProductButton).click()
