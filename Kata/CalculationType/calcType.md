# Python code to Find the calculation type

## Description
You have to create a function calcType, which receives 3 arguments: 2 numbers, and the result of an unknown operation performed on them (also a number).

Based on those 3 values you have to return a string, that describes which operation was used to get the given result.

The possible return strings are: "addition", "subtraction", "multiplication", "division".

## BDD
The user should:
  -Input 3 arguments to check their calculation type
|            Input           |           Output         |
|----------------------------|--------------------------|
| Num1 = 2, Num2 = 2,Num = 4 | Addition, Multiplication |
| Num1 = 1, Num2 = 3,Num = 5 | Invalid                  |

## Pseudocode
- Define function to check calculation type.
- Declare variable x,y,z to hold the value of argument 1,2 and 3
- IF condition to check whether x (calculation type) y are equal z
- IF true return calculation type

## Python code
```text
# def calcType():
    
#     num1 = int(input("Enter First number\n"))
    
#     num2 = int(input("Enter Second number\n"))
    
#     num3 = int(input('Enter results of num1 and num2\n'))
    
#     if num1 + num2 == num3:
#         result = "addition"
#     elif num1 - num2 == num3:
#         result="subtraction"
#     elif num1/num2 == num3:
#         result ="division"
#     elif num1*num2 == num3:
#         result ="multiplication"
#     else:
#         result="wrong input"
#     print (result)
# calcType()

# def calcType(num1,num2,num3):
    
#     if num1 + num2 == num3:
#         result = "addition"
#     elif num1 - num2 == num3:
#         result="subtraction"
#     elif num1/num2 == num3:
#         result ="division"
#     elif num1*num2 == num3:
#         result ="multiplication"
#     else:
#         result="wrong input"
#     print (result)
# calcType(2,2,4)
def calcType():
    num1=20
    num2=20
    num3=40
    if num1 + num2 == num3:
        result = "addition"
    elif num1 - num2 == num3:
        result="subtraction"
    elif num1/num2 == num3:
        result ="division"
    elif num1*num2 == num3:
        result ="multiplication"
    else:
        result="wrong input"
    print (result)
calcType()
```
## Kata link
[viewkata](https://www.codewars.com/kata/5aca48db188ab3558e0030fa)
