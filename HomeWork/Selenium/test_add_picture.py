from selenium.webdriver.support import expected_conditions as EC

import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from HomeWork.Selenium.fixtures import login_page, login, dashbord_actions, add_product, add_products, dashbord_page, \
    products_page, product_page, image_page, add_image
from selenium.webdriver.common.by import By


class TestAddProduct:
    @pytest.mark.usefixtures("login", "dashbord_actions", "add_products", "add_image")
    def test_add_product(self, products_page, product_page, image_page, brw):
        webdriver.ActionChains(brw).send_keys(Keys.ESCAPE).perform()
        try:
            WebDriverWait(brw, 3).until(EC.alert_is_present())
            brw.switch_to.alert.accept()
        except Exception:
            raise TimeoutError('Alert not found!')
        product_page.choose_image()
        product_page.edit_image()
        image_page.set_image1()
        product_page.save_button()
        try:
            products_page.check_successful_modified("Success: You have modified products!")
        except Exception:
            raise TimeoutError('Add Failed!')
