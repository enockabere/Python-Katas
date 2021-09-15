# Python code to print the number of stars till the number entered

## Description
Write a program called stars.py. It should prompt the user for a number, and it should print the number of stars till the number entered.

## BDD
The user should:
  -Input a number, and it should print the number of stars till the number entered.

|    Input         |   Output  |
|------------------|-----------|
| number eg = 3    |  *        |
|                  |  **       |
|                  |  ***      |

## Pseudocode
- Define function to generate stars
- Declare variable num to accept input and store the number of rows
- Loop to handle number of rows
- Loop to handle number of column
- Print stars in a new line

## Python code
```text
def stars():
    num = int(input("Enter a number\t"))
    #loop to handle number of rows which is num
    for i in range(0, num):
        #loop to handle number of column
        for j in range(0, i + 1):
            #print stars in a line
           print("*",end='')
           #end line after each row
        print('\n')
stars()
```

