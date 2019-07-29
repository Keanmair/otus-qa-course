class TestSuiteSocket:
    def test_http_socket(self, http):
        header, retcode, retresult, headers = http
        assert retresult == "OK"