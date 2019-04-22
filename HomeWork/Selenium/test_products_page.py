import pytest
from HomeWork.Selenium.models.page_objects.page_objects import LoginPage, ProductsPage, Dashboard
import time


@pytest.fixture
def login_page(brw):
    return LoginPage(brw)


@pytest.fixture
def dashbord_page(brw):
    return Dashboard(brw)


@pytest.fixture
def products_page(brw):
    return ProductsPage(brw)


@pytest.fixture
def login(login_page):
    login_page.set_username("admin")
    login_page.set_password("PASSWORD")
    login_page.login_button()
    time.sleep(5)


@pytest.fixture
def dashbord_actions(dashbord_page):
    dashbord_page.menu_catalog_button()
    dashbord_page.categories_button()


@pytest.mark.usefixtures("login_page")
class TestAddProduct:
    @pytest.mark.usefixtures("login", "dashbord_actions")
    def test_add_product(self, products_page):
        products_page.add_product_button()
        time.sleep(5)
