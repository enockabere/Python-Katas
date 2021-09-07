# Python code to check what a string end with.

## Description
I will use python inbuilt method  **endswith()**  returns True if a string ends with a specified value otherwise False.

## BDD
The user should:
  -Input a string to check whether it ends with "abc"
|    Input         |   Output  |
|------------------|-----------|
| String eg = "bc" | True      |
| String eg = "d"  | False     |

## Pseudocode
- Define function to check what a string ends with.
- Declare variable x to hold the value which is going to be checked against
- Declare  variable y to accept input and store a string
- use endswith() method to check if x ends with y.
- Return True or False

## Python code
```text
def ends():
    checkString = "abc"
    
    yourString = input("Enter string to check\n")
    
    result = checkString.endswith(yourString)
    
    print (result)
ends()
```
## Kata link
[viewkata](https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d)
