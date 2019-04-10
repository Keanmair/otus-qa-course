def test_store(brw):
    brw.get(("http://192.168.77.43/opencart//"))
    assert brw.find_element_by_class_name('col-sm-4').text == 'Your Store', "No main page found."
