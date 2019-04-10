def test_store(brw):
    assert brw.find_element_by_class_name('col-sm-4').text == 'Your Store', "No main page found."
