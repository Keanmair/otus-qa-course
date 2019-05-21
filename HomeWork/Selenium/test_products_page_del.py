import pytest
from HomeWork.Selenium.fixtures import login_page, login, dashbord_actions_categories, add_product, add_products, dashbord_page, products_page, product_page


class TestDelProduct:
    @pytest.mark.usefixtures("login", "dashbord_actions_categories", "add_products", "add_product")
    def test_del_product(self, products_page):
        products_page.driver.refresh()
        products_page.del_check_box()
        products_page.delete_product_button()
        products_page.driver.switch_to.alert.accept()
        assert products_page.check_successful_modified("Success: You have modified products!"), "Products not modified!"
