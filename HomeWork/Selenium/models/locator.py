from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    Username = (By.ID, "input-username")
    Password = (By.ID, "input-password")
    ForgottenPassword = (By.XPATH, "//a[text()='Forgotten Password']")
    LoginButton = (By.CLASS_NAME, "btn-primary")
    Base_opencart = (By.XPATH, "//a[text()='OpenCart']")
    Head_opencart = (By.CLASS_NAME, "navbar-brand")


class ForgottenPasswordLocators(object):
    Email = (By.CLASS_NAME, "form-control")
    ResetButton = (By.CLASS_NAME, "btn-primary")
    BackButton = (By.CLASS_NAME, "btn-default")


class DashboardLocators(object):
    MenuCatalog = (By.ID, "menu-catalog")
    Products = (By.XPATH, "//a[text()='Products']")


class ProductsPageLocators(object):
    AddProductButton = (By.XPATH, "//a[@data-original-title='Add New']")
    DeleteProductButton = (By.XPATH, "//button[@data-original-title='Delete']")
    DelCheckBox = (By.NAME, "selected[]")
    EditProductButton = (By.XPATH, "//a[@data-original-title='Edit']")
    SuccessfulModified = (By.CSS_SELECTOR, ".alert")


class ProductLocators(object):
    Product_name = (By.ID, "input-name1")
    Meta_tag = (By.ID, "input-meta-title1")
    Data = (By.XPATH, "//a[text()='Data']")
    Image = (By.XPATH, "//a[text()='Image']")
    Model = (By.ID, "input-model")
    DefaultImageIcon = (By.XPATH, "//img[@src='http://192.168.77.43/opencart/image/cache/no_image-100x100.png']")
    SaveButton = (By.XPATH, "//button[@data-original-title='Save']")
    EditImageButton = (By.ID, "button-image")
    AddImageButton = (By.XPATH, "//button[@data-original-title='Add Image']")
    UploadImageButton = (By.XPATH, "//button[@data-original-title='Upload']")
    InputManager = (By.XPATH, "//input[@name='file[]']")


class ImagesLocators(object):
    Image_1 = (By.XPATH, "//a[@href='http://192.168.77.43/opencart/image/catalog/1.png']")
    Image_2 = (By.XPATH, "//a[@href='http://192.168.77.43/opencart/image/catalog/2.jpg']")
    Image_3 = (By.XPATH, "//a[@href='http://192.168.77.43/opencart/image/catalog/3.jpg']")
    NewImage_1 = (By.XPATH, "//img[@src='http://192.168.77.43/opencart/image/cache/catalog/1-100x100.png']")
    NewImage_3 = (By.XPATH, "//img[@src='http://192.168.77.43/opencart/image/cache/catalog/3-100x100.jpg']")
    NewImage_2 = (By.XPATH, "//img[@src='http://192.168.77.43/opencart/image/cache/catalog/2-100x100.jpg']")
