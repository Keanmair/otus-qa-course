import pytest
from HomeWork.Selenium.fixtures import login_page, login


@pytest.mark.usefixtures("login_page")
class TestLoginPage:

    @pytest.mark.usefixtures("login")
    def test_login(self, brw):
        assert brw.find_element_by_class_name('close'), "Invalid locator!"

