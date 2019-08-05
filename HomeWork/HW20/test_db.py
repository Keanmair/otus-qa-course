class TestSuite:

    def test_add_product(self, add_product):
        expected_result, current_result = add_product
        assert expected_result in current_result

    def test_modify_product(self, modify_product):
        expected_result, current_result = modify_product
        assert expected_result in current_result

    def test_delete_product(self, delete_product):
        expected_result, current_result = delete_product
        assert expected_result in current_result
