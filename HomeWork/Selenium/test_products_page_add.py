import pytest

from HomeWork.Selenium.fixtures import login_page, login, dashbord_actions, add_product, add_products, dashbord_page, products_page, product_page
from HomeWork.Selenium.models.page_objects.page_objects import LoginPage, ProductsPage, Dashboard, ProductPage


@pytest.mark.usefixtures("login_page")
class TestAddProduct:
    @pytest.mark.usefixtures("login", "dashbord_actions")
    def test_add_product(self, products_page, product_page):
        products_page.add_product_button()
        product_page.set_product_name("1")
        product_page.set_meta_tag("test")
        product_page.data_button()
        product_page.set_model("test")
        product_page.save_button()
        assert products_page.check_successful_modified("Success: You have modified products!"), "Products not modified!"
