from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    Username = (By.ID, "input-username")
    Password = (By.ID, "input-password")
    LoginButton = (By.CLASS_NAME, "btn-primary")


class DashboardLocators(object):
    Menu = (By.ID, "menu-design")
    Constructor = (By.XPATH, "//a[text()='Конструктор Меню']")


class DragNDrop(object):
    SourceElem = (By.XPATH, "//dl[@class='custommenu-item-bar']//span[text()='Контакты']")
    DestElem = (By.XPATH, "//dl[@class='custommenu-item-bar']")
    SuccsesDrag = (By.XPATH, "//ul[@id='custommenu-to-edit']/li[1]//span[@class='custommenu-item-title']")
