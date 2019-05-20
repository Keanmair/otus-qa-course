
import pytest
from selenium.webdriver import ActionChains

from HomeWork.OpenCartDemo.fixtures import login_page, login, dashbord_page, dashbord_actions, construct_page
from HomeWork.OpenCartDemo.models.locator import DragNDrop


class TestDrag:
    @pytest.mark.usefixtures("login", "dashbord_actions")
    def test_drag_n_drop(self, construct_page):
        construct_page.drag_n_drop()
        assert construct_page.succsefull_drag("Контакты"), "Unsuccesfull Drag'n'Drop"
