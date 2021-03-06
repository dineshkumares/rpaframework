*** Settings ***
Library         RPA.Browser    locators_path=${LOCATORS}  run_on_failure=${NONE}
Suite Setup     Open Available Browser  about:blank  headless=${TRUE}
Suite Teardown  Close All Browsers
Default Tags    RPA.Browser

*** Variables ***
${RESOURCES}    ${CURDIR}${/}..${/}resources
${LOCATORS}     ${RESOURCES}${/}locators.json
${ALERT_HTML}   file://${RESOURCES}${/}alert.html


*** Tasks ***
Does alert contain
    Go To                 ${ALERT_HTML}
    Click Element         //button
    ${res}                Does Alert Contain  after
    Handle Alert          DISMISS

Does alert not contain
    Go To                 ${ALERT_HTML}
    Click Element         //button
    ${res}                Does Alert Not Contain  afterx
    Handle Alert          DISMISS

Basic browser open and usage
    [Tags]  skip
    Open available browser          https://www.google.com/    headless=${TRUE}
    Wait Until Element Is Visible   q
    Input Text                      q  Robocorp
    Click Element                   q
    Press keys                      q    ENTER
    Sleep                           3s
    Screenshot

Check span value
    [Tags]  skip
    Open available Browser    https://www.w3schools.com/tags/att_span.asp    headless=${TRUE}
    ${val}=    Get Value        class:dotcom
    ${elem}=   Get WebElement   class:dotcom
    Log        ${elem.text}

Locator aliases
    [Tags]  skip
    Open Available Browser    https://robotsparebinindustries.com/    headless=${TRUE}
    Input Text      alias:RobotSpareBin.Username    maria
    Input Text      alias:RobotSpareBin.Password    thoushallnotpass
    Submit Form
    Click button when visible   id:logout
