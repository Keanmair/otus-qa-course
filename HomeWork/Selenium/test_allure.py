import pytest
from HomeWork.Selenium.models.page_objects.page_objects import LoginPage
from HomeWork.Selenium.fixtures import login_page, login, dashbord_actions_categories, add_product, add_products, dashbord_page, \
    products_page, product_page


class TestLoginPage:

    @pytest.mark.usefixtures("login")
    def test_login(self, brw):
        brw.refresh()
        assert brw.find_element_by_class_name(
                'panel-title').text == 'World Map', "Invalid locator!"


# class TestAddProduct:
    @pytest.mark.usefixtures("dashbord_actions_categories")
    def test_add_product(self, products_page, product_page):
        pytest.skip()
        products_page.add_product_button()
        product_page.set_product_name("1")
        product_page.set_meta_tag("test")
        product_page.data_button()
        product_page.set_model("test")
        product_page.save_button()
        # assert products_page.check_successful_modified("Success: You have modified products!"), "Products not modified!"
        try:
            products_page.check_successful_modified("Success: You have modified products!")
        except Exception:
            raise TimeoutError('Add Failed!')