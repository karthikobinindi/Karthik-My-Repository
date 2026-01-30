*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}       https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${browser}   firefox

*** Keywords ***
Open OrangeHRM
    Open Browser    ${url}    ${browser}
    Maximize Browser Window
    Set Selenium Timeout    15s
    Set Selenium Implicit Wait    5s
    Wait Until Element Is Visible    name=username    20s

OrangeHRM Login
    [Arguments]    ${username}    ${password}
    Input Text    name=username    ${username}
    Input Text    name=password    ${password}
    Capture Page Screenshot    beforelogin.png
    Click Button    xpath=//button[@type='submit']
    Wait Until Element Is Visible    xpath=//span[@class='oxd-userdropdown-tab']    20s
    Capture Page Screenshot    afterlogin.png
    Close Browser

*** Test Cases ***
Valid Login Test
    Open OrangeHRM
    OrangeHRM Login    Admin    admin123
