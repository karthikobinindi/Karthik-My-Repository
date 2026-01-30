*** Settings ***
Library    SeleniumLibrary
library    SeleniumLibrary
Library     DataDriver    file=testdata.xlsx    Sheet1
Test Template    orangehrmlogin with Excel


*** Variables ***
${url}      https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${browser}      firefox


*** Keywords ***
open orangehrm
    open browser    ${url}     ${browser}
    maximize browser window
orangehrmlogin with Excel
    [Arguments]    ${username}  ${password}
    Input text    name=username    ${username}
    input text      name=password    ${password}
    sleep           5s
     capture page screenshot    beforelogin.png
    click button    xpath=//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button
     sleep           5s
    capture page screenshot    afterlogin.png
    close browser

*** Test Cases ***
Robo6.robot
    open orangehrm
     sleep           5s
   orangehrmlogin with Excel
    ${username}   ${password}
