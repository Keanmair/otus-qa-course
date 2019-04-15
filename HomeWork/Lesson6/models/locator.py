from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    Username = (By.ID, "input-username")
    Password = (By.ID, "input-password")
    ForgottenPassword = (By.XPATH, "//a[text()='Forgotten Password']")
    LoginButton = (By.CLASS_NAME, "btn-primary")
    Base_opencart = (By.XPATH, "//a[text()='OpenCart']")
    Head_opencart = (By.CLASS_NAME, "navbar-brand")
