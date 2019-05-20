import pytest

from HomeWork.OpenCartDemo.models.page_objects.page_objects import LoginPage, Dashboard, Drag


@pytest.fixture(scope="module")
def login_page(brw):
    return LoginPage(brw)


@pytest.fixture(scope="module")
def dashbord_page(brw):
    return Dashboard(brw)


@pytest.fixture(scope="module")
def construct_page(brw):
    return Drag(brw)


@pytest.fixture(scope="function")
def login(login_page):
    login_page.set_username("demo")
    login_page.set_password("demo")
    login_page.login_button()


@pytest.fixture(scope="function")
def dashbord_actions(dashbord_page):
    dashbord_page.menu_button()
    dashbord_page.constructor_button()
