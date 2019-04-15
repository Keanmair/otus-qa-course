import pytest
from HomeWork.Lesson6.models.page_objects.page_objects import LoginPage
import time


@pytest.fixture
def login_page(brw):
    return LoginPage(brw)


@pytest.fixture
def login(login_page):
    login_page.set_username("incorrectlogin")
    login_page.set_password("incorrectpassword")
    login_page.login_button()


@pytest.mark.usefixtures("login_page")
class TestLoginPage:

    @pytest.mark.usefixtures("login")
    def test_login(self, brw):
        assert brw.find_element_by_class_name('close'), "Invalid locator!"
        # assert brw.find_element_by_class_name(
        #     'alert-dismissible').text == 'Invalid token session. Please login again.', "Invalid locator!"
