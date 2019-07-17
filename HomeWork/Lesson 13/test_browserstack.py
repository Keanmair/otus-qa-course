from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# desired_cap = {
#     'browser': 'Chrome',
#     'browser_version': '73.0',
#     'os': 'Windows',
#     'os_version': '10',
#     'resolution': '1024x768',
#     'name': 'Bstack-[Python] Sample Test'
# }
#
# driver = webdriver.Remote(
#     command_executor='http://semyonkorneev1:pTvcn8PcGsdvnzpegsSG@hub.browserstack.com:80/wd/hub',
#     desired_capabilities=desired_cap)



capabilities = {
    "browserName": "chrome",
    "version": "70.0",
    "enableVNC": True,
    "enableVideo": False
}

driver = webdriver.Remote(
    command_executor="http://selenoid:4444/wd/hub",
    desired_capabilities=capabilities)

driver.get("http://www.google.com")
if not "Google" in driver.title:
    raise Exception("Unable to load google page!")
elem = driver.find_element_by_name("q")
elem.send_keys("BrowserStack")
elem.submit()
print(driver.title)
driver.quit()
