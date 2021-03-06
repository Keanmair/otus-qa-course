*** Keywords ***
OpenAdminPage
    Open Browser  http://192.168.77.43/admin/  Chrome
    Title Should be  Administration


InputUsername
    [Arguments]  ${user}
    Input Text   username  ${user}


InputPassword
    [Arguments]  ${password}
    Input Text    id:input-password  ${password}
    sleep  5s


Login
    InputUsername  admin
    InputPassword  PASWWORD
    Click Button  Login
    Title Should be  Dashboard


FailLogin
    InputUsername    admin
    InputPassword    admin
    Click Button   Login

AssertFailtNotification
    Get WebElement  xpath://*[contains(text(), 'No match for Username and/or Password')]

AssertSuccessNotification
    Get WebElement  xpath://*[contains(text(), 'Success: You have modified products!')]