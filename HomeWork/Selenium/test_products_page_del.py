import pytest
from HomeWork.Selenium.models.page_objects.page_objects import LoginPage, ProductsPage, Dashboard, ProductPage
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
def product_page(brw):
    return ProductPage(brw)


@pytest.fixture
def login(login_page):
    login_page.set_username("admin")
    login_page.set_password("PASSWORD")
    login_page.login_button()


@pytest.fixture
def dashbord_actions(dashbord_page):
    dashbord_page.menu_catalog_button()
    dashbord_page.categories_button()


@pytest.fixture
def add_products(products_page):
    products_page.add_product_button()


@pytest.fixture
def add_product(product_page):
    product_page.set_product_name("1")
    product_page.set_meta_tag("test")
    product_page.data_button()
    product_page.set_model("test")
    product_page.save_button()


@pytest.mark.usefixtures("login_page")
class TestEditProduct:
    @pytest.mark.usefixtures("login", "dashbord_actions", "add_products", "add_product")
    def test_edit_product(self, products_page):
        products_page.driver.refresh()
        products_page.del_check_box()
        products_page.delete_product_button()
        products_page.driver.switch_to.alert.accept()
        assert products_page.check_successful_modified("Success: You have modified products!"), "Products not modified!"