## Description
Implement a program that takes 3 form inputs or from the terminal, and stores them in three variables. Return the largest of the three. Do this without using the the inbuilt max () function!
The goal of this exercise is to think about some internals that programs normally take care of for us. 
Extras:
If the number is a multiple of 4, display out a different message.
 
## BDD
The user should:
  -Input 3 integers to find the largest
|          Input            |      Output      |
|---------------------------|------------------|
|    num1= 1, num2=3,num3=5 | 5 is the largest | 

## Pseudocode
- Define function to check three numbers
- Declare a variable x,y,z to accept input and store 3 integers
- Create a list a and append the three integers to it.
- Sort the list of integers and loop through the list to check whether there is number that is multiple of 4
- If there is a multiple of 4 return it and the largest number
- Else return largest number
## Python code
```text
def numbers():
    numList = []
    num1=int(input("Enter num1\n"))
    num2=int(input("Enter num2\n"))
    num3=int(input("Enter num3\n"))
    
    numList.append(num1)
    numList.append(num2)
    numList.append(num3)
    
    newList=sorted(numList)
    for x in newList:
        if x % 4 == 0:
            print ('Woow!',x,'is a multiple of 4','*'*4)
    print('*'*4,newList.pop(),"IS THE LARGEST",'*'*4)
numbers()
```
