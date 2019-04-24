import pytest

from HomeWork.Selenium.fixtures import login_page, login, dashbord_actions, add_product, add_products, dashbord_page, products_page, product_page
from HomeWork.Selenium.models.page_objects.page_objects import LoginPage, ProductsPage, Dashboard, ProductPage
import time


class TestEditProduct:
    @pytest.mark.usefixtures("login", "dashbord_actions", "add_products", "add_product")
    def test_edit_product(self, products_page, product_page):
        products_page.driver.refresh()
        products_page.edit_product_button()
        product_page.set_product_name("111")
        product_page.save_button()
        assert products_page.check_successful_modified("Success: You have modified products!"), "Products not modified!"