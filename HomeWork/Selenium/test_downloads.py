import pytest
from HomeWork.Selenium.fixtures import login_page, login, dashbord_actions_categories, dashbord_page, dashbord_actions_downloads, downloads_page


class TestDownloadFile:
    @pytest.mark.usefixtures("login", "dashbord_actions_downloads")
    def test_del_product(self, downloads_page):
        downloads_page.add_new_download_button()
        downloads_page.set_download_name("test")
        downloads_page.set_file_name("test")
        downloads_page.set_mask_name("test")
        downloads_page.upload_file_button()
        downloads_page.add_download_file("/home/korneev/Pictures/1.png")
        downloads_page.save_download_button()
        assert downloads_page.succsefull_download("test"), "Unsuccessful Download"

