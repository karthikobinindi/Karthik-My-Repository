*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}        https://www.google.com
${BROWSER}    chrome
${EXPECTED_TITLE}    Google

*** Test Cases ***
Verify Page Title and Screenshot
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Page Contains Element    name=q    10s
    Title Should Be    ${EXPECTED_TITLE}
    Capture Page Screenshot    google_homepage.png
    Close Browser
