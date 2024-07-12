*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${login}    https://google.com/
${username}    User
${password}    password


*** Test Cases ***
validate the browser open
    Open Browser    ${login}    chrome
    Input Text    ${username}
    Input Text    ${password}
    Sleep    5