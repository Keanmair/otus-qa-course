import time


class TestSuiteSSH:

    def test_apache_restart(self, apache_restart_test):
        expected_result, current_result = apache_restart_test
        assert expected_result == current_result

    def test_mysql_restart(self, mysql_restart_test):
        expected_result, current_result = mysql_restart_test
        assert expected_result == current_result

    def test_reset(self, is_base_page, server_reset):
        server_reset
        time.sleep(150)
        expected_result, current_result = is_base_page
        assert expected_result == current_result
