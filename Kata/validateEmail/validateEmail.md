# Code to validate email
## Description
Write a program which accepts email as form input or from terminal. Validate the email by checking if it contains an “@” symbol and “.” symbol. 
## BDD
The user should:
  -Input a string to check it is a valid email
|          Input            |   Output  |
|---------------------------|-----------|
| email eg = user@gmail.com |   Valid   |
| email eg = user.com       | invalid   |
## Pseudocode
- Define function to validate email
- Declare a variable x to accept input and store an email address
- If condition to check whether email is valid
- Return a string
## Python code
```text
def email():
    address= input("Enter email address to validate\n")
    x = list(address)
    
    if "@" in x and "." in x:
        print('*'*2,address, 'is valid','*'*2)
    else:
        print('*'*2,address, 'is invalid','*'*2)
email()
```
