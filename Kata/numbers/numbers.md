## Description
Implement a program that takes 3 form inputs or from the terminal, and stores them in three variables. Return the largest of the three. Do this without using the the inbuilt max () function!
The goal of this exercise is to think about some internals that programs normally take care of for us. 
Extras:
If the number is a multiple of 4, display out a different message.
 
## BDD
The user should:
  -Input an integer to check whether is odd or even
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
