# Find out if number is odd or even
## Description
Create a function that takes an integer as an argument and returns “Even” for even numbers or “Odd” for odd numbers.
## BDD
The user should:
  -Input an integer to check whether is odd or even
|   Input        |  Output  |
|----------------|----------|
| Integer eg = 6 | even     |
|----------------|----------|
| Integer eg = 3 | odd      |
## Pseudocode
- Define function to check whether number is odd or even
- Declare a variable to accept input and store an integer
- If condition to check whether number is odd or even
- Return a string
## Python code
```text
def even_odd():
    num = int(input(‘Enter number to find whether is even or odd\n’))
    if num % 2 ==0:
        print(f”{num} is an even number”)
    else:
        print(f”{num} is an odd number”)
even_odd()
```
## Kata link
[viewkata](https://www.codewars.com/kata/53da3dbb4a5168369a0000fe)