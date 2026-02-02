*** Settings ***

#IF Condition
*** Test Cases ***
IF Condition Example
   ${age}=  Set Variable  20
   IF   ${age}>= 18
      Log  Eligible to vote
   END

#IF Else

*** Test Cases ***
IF ELSE Example
   ${num}=   Set Variable   5
   IF  ${num} > 10
     Log   Greater than 10
   ELSE
      Log   Less than or equal tp 10
   END

#IF ELSE IF ELSE
*** Test Cases ***

IF ELSE IF Example
   ${marks}=  Set Variable   75
   IF     ${marks}>=90
       Log   Grade A
   ELSE IF    ${marks}>=75
       Log   Grade B
   ELSE
       Log   Grade C
   END

#IN LINE IF
*** Test Cases ***
FOR Loop Basic
   FOR   ${item}  IN  one  two  three
     Log  item:${item}
   END
