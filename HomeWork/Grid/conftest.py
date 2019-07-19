import pytest


def pytest_addoption(parser):
    parser.addoption("--add_browser", action="store", type=str, default="Chrome")
    parser.addoption("--url", action="store", type=str, default="main")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--add_browser")


@pytest.fixture(scope="session")
def ext_url(request):
    return request.config.getoption("--url")
