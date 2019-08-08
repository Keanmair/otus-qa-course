*** Settings ***
Documentation    Suite description

Library ./mylib.py

*** Variables ***
${NAME_ADMIN} admin
${PASS_ADMIN} password
${EMAIL_MAIN} qa@gmail.com
${PASS_MAIN} qapass

*** Test Cases ***
Login Admin
    Login Admin
    Open Page
    Set Username   ${NAME_ADMIN}
    Set Password   ${PASS_ADMIN}
    Submit
    Close

Login Main
    Login Main
    Open Page
    Set Email   ${EMAIL_MAIN}
    Set Password   ${PASS_MAIN}
    Submit
    Close
