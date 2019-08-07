*** Settings ***
Library  DatabaseLibrary

*** Variables ***
${DBPass}         ${EMPTY}

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


Login
    InputUsername  admin
    InputPassword  admin
    Click Button  Login
    Title Should be  Dashboard


FailLogin
    InputUsername    admin
    InputPassword    admin1
    Click Button   Login

AssertFailtNotification
    Get WebElement  xpath://*[contains(text(), 'No match for Username and/or Password')]

AssertSuccessNotification
    Get WebElement  xpath://*[contains(text(), 'Success: You have modified products!')]


ConnectToDB
    Connect To Database  pymysql  bitnami_opencart  bn_opencart  ${DBPass}  192.168.77.43   4407

AddProduct
    OpenAdminPage
    Login
    Click Element  xpath://a[contains(text(),'Catalog')]
    Click Element  xpath://a[contains(text(),'Products')]
    Click Element  xpath://a[@data-original-title='Add New']
    Input text  name:product_description[1][name]   Acer
    Input text  name:product_description[1][meta_title]   Test Acer
    Click Element  partial link:Data
    Input text  name:model   Test Acer
    Click element  xpath://button[@data-original-title='Save']
    AssertSuccessNotification

DeleteProduct
    OpenAdminPage
    Login
    Click Element   xpath://a[contains(text(),'Catalog')]
    Click Element   xpath://a[contains(text(),'Products')]
    Select Checkbox  xpath://td[contains(text(),'Acer')]/parent::*//input
    Click Element   xpath://button[@data-original-title='Delete']
    Handle Alert
    AssertSuccessNotification

SelectFromDB
    ${query} =  Query  select count(*) from oc_product;
    [return]  ${query[0][0]}