from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    Username = (By.ID, "input-username")
    Password = (By.ID, "input-password")
    ForgottenPassword = (By.XPATH, "//a[text()='Forgotten Password']")
    LoginButton = (By.CLASS_NAME, "btn-primary")
    Base_opencart = (By.XPATH, "//a[text()='OpenCart']")
    Head_opencart = (By.CLASS_NAME, "navbar-brand")


class ForgottenPasswordLocators(object):
    Email = (By.CLASS_NAME, "form-control")
    ResetButton = (By.CLASS_NAME, "btn-primary")
    BackButton = (By.CLASS_NAME, "btn-default")


class DashboardLocators(object):
    MenuCatalog = (By.ID, "menu-catalog")
    Categories = (By.XPATH, "//a[text()='Products']")


class ProductsPageLocators(object):
    AddProductButton = (By.XPATH, "//a[@data-original-title='Add New']")
    DeleteProductButton = (By.XPATH, "//button[@data-original-title='Delete']")


