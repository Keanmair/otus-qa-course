import pytest
from HomeWork.Selenium.models.page_objects.page_objects import LoginPage
from HomeWork.Selenium.fixtures import login_page, login


class TestLoginPage:

    @pytest.mark.usefixtures("login")
    def test_login(self, brw):
        brw.refresh()
        assert brw.find_element_by_class_name(
                'panel-title').text == 'World Map', "Invalid locator!"
