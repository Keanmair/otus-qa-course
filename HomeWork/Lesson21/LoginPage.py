
class BasePage(object):
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def navigate(self):
        self.driver.get(self.url)
        self.driver.maximize_window()


class LoginPage(BasePage):
    def _get_title_(self):
        return self.driver.title

    def get_title(self):
        return self._get_title_()
