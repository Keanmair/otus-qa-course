from selenium import webdriver

from HomeWork.Selenium.models.locator import LoginPageLocators, ForgottenPasswordLocators, ProductsPageLocators, \
    DashboardLocators, ProductLocators, ImagesLocators
from HomeWork.Selenium.models.page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class LoginPage(BasePage):

    def set_username(self, username):
        self.find_element(LoginPageLocators.Username).send_keys(username)

    def set_password(self, password):
        self.find_element(LoginPageLocators.Password).send_keys(password)

    def login_button(self):
        self.find_element(LoginPageLocators.LoginButton).click()

    def clear_login(self):
        self.clear_text(self.find_element(LoginPageLocators.Username))

    def clear_password(self):
        self.clear_text(self.find_element(LoginPageLocators.Password))

    def forgotten_password_button(self):
        self.find_element(LoginPageLocators.ForgottenPassword).click()


class ForgottenPage(BasePage):

    def set_email(self, email):
        self.find_element(ForgottenPasswordLocators.Email).send_keys(email)

    def reset_button(self):
        self.find_element(ForgottenPasswordLocators.ResetButton).click()

    def back_button(self):
        self.find_element(ForgottenPasswordLocators.BackButton).click()


class Dashboard(BasePage):

    def menu_catalog_button(self):
        self.find_element(DashboardLocators.MenuCatalog).click()

    def categories_button(self):
        self.find_element(DashboardLocators.Products).click()


class ProductsPage(BasePage):

    def add_product_button(self):
        self.find_element(ProductsPageLocators.AddProductButton).click()

    def del_check_box(self):
        self.find_element(ProductsPageLocators.DelCheckBox).click()

    def delete_product_button(self):
        self.find_element(ProductsPageLocators.DeleteProductButton).click()

    def edit_product_button(self):
        self.find_element(ProductsPageLocators.EditProductButton).click()

    def check_successful_modified(self, text):
        current_text = self.find_element(ProductsPageLocators.SuccessfulModified).text
        if text in current_text:
            return True
        else:
            return False


class ProductPage(BasePage):
    def set_product_name(self, product_name):
        self.find_element(ProductLocators.Product_name).send_keys(product_name)

    def set_meta_tag(self, meta_tag):
        self.find_element(ProductLocators.Meta_tag).send_keys(meta_tag)

    def data_button(self):
        self.find_element(ProductLocators.Data).click()

    def set_model(self, model):
        self.find_element(ProductLocators.Model).send_keys(model)

    def save_button(self):
        self.find_element(ProductLocators.SaveButton).click()

    def image_button(self):
        self.find_element(ProductLocators.Image).click()

    def add_image(self):
        self.find_element(ProductLocators.AddImageButton).click()

    def choose_default_image(self):
        self.find_element(ProductLocators.DefaultImageIcon).click()

    def edit_image(self):
        self.find_element(ProductLocators.EditImageButton).click()

    def upload_image(self):
        self.find_element(ProductLocators.UploadImageButton).click()

    def add_custom_image(self, text):
        self.wait_element_presence(ProductLocators.InputManager).send_keys(text)


class SetImage(BasePage):
    def set_image1(self):
        self.find_element(ImagesLocators.Image_1).click()

    def set_image2(self):
        self.find_element(ImagesLocators.Image_2).click()

    def set_image3(self):
        self.find_element(ImagesLocators.Image_3).click()

    def check_image_1(self):
        assert self.assert_element_presence(ImagesLocators.NewImage_1), "No such image"

    def check_image_2(self):
        assert self.assert_element_presence(ImagesLocators.NewImage_2), "No such image"

    def check_image_3(self):
        assert self.assert_element_presence(ImagesLocators.NewImage_3), "No such image"
