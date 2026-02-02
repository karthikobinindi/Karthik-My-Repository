*** Settings ***
Library    RequestsLibrary

*** Variables ***
${baseurl}  http://127.0.0.1:5000
*** Test Cases ***

#GET ALL
Verify Get All User
        Create Session    mysession             ${baseurl}
        ${response}=  GET On Session    mysession   /users
        Status Should Be    200      ${response}
        ${res_jon}=     To Json    ${response.content}
        log       ${res_jon}=   console=True

#GET1
Verify Get Single User
        Create Session    mysession             ${baseurl}
        ${response}=  GET On Session    mysession   /users/2
        Status Should Be    200      ${response}
        ${res_jon}=     To Json    ${response.content}
        log       ${res_jon}=   console=True

#Verify Get Single User not Found
#        Create Session    mysession             ${baseurl}
#        ${response}=  GET On Session    mysession   /users/99
#        Status Should Be   404      ${response}
#        ${res_jon}=     To Json    ${response.content}
#        log       ${res_jon}=   console=True


#POST
Verify Create New User
    Create Session    mysession    ${baseurl}
    ${body}=    Create Dictionary    id=4    name=Karthik
    ${headers}=    Create Dictionary    Content-Type=application/json
    ${response}=    POST On Session    mysession    /users    json=${body}    headers=${headers}
    Status Should Be    201    ${response}
    ${res_json}=    To Json    ${response.content}
    Log    ${res_json}    console=True

#PUT
Verify Update User Using PUT
    Create Session    mysession    ${baseurl}
    ${body}=    Create Dictionary    id=4    name=Rahul
    ${headers}=    Create Dictionary    Content-Type=application/json
    ${response}=    PUT On Session    mysession    /users/4    json=${body}    headers=${headers}
    Status Should Be    200    ${response}
    ${res_json}=    To Json    ${response.content}
    Log    ${res_json}    console=True

#PATCH
Verify Update User Using PATCH
    Create Session    mysession    ${baseurl}
    ${body}=    Create Dictionary    name=UpdatedName
    ${headers}=    Create Dictionary    Content-Type=application/json
    ${response}=    PATCH On Session    mysession    /users/4    json=${body}    headers=${headers}
    Status Should Be    200    ${response}
    Log    ${response.json()}    console=True

#DELETE
Verify Delete User
    Create Session    mysession    ${baseurl}
    ${response}=    DELETE On Session    mysession    /users/4
    Status Should Be    200    ${response}
    Log    User deleted successfully    console=True
