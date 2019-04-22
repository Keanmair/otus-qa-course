import pytest
from HomeWork.Selenium.models.page_objects.page_objects import LoginPage


@pytest.fixture
def login_page(brw):
    return LoginPage(brw)


@pytest.fixture
def login(login_page):
    login_page.set_username("admin")
    login_page.set_password("PASSWORD")
    login_page.login_button()


@pytest.mark.usefixtures("login_page")
class TestLoginPage:

    @pytest.mark.usefixtures("login")
    def test_login(self, brw):
        brw.refresh()
        assert brw.find_element_by_class_name(
                'panel-title').text == 'World Map', "Invalid locator!"
