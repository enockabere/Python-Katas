# Python code to create a string from a list of strings, separated by space.

## Description
Write function which will create a string from a list of strings, separated by space.

## BDD
The user should:
  -Input a list  turn into a string
  - Input should be entered in words then the program finds spaces in entered sentence to create a list

|           Input              |       Output       |
|------------------------------|--------------------|
| list eg = ["Hello", "World"] |    Hello World     |


## Pseudocode

- Define **function** to turn list into string
- Declare  variable **x** to accept input and store a string
- Use **split()** to change variabe **x** into a list and store it in variable **y**
- Use **join()** method to change variable **y** into a string and store it in variable **z**. 
- **Return** z

## Python code

```text
def listTostring():
    mylist=['hello','world']
    
    result = " ".join(mylist)
    
    print(result)
listTostring()

#example to make a string a list and make it a string again

def listTostring():
    
    raw = input("Enter a list of words\n")
    
    #change string to list using split method
    result = list(raw.split(" "))
    
    #change list to string
    result2 = " ".join(result)
    
    print('*'*5,result ,'*'*2, 'CHANGED TO','*'*5,'\n',result2)
listTostring()
```
## Kata link
[viewkata](https://www.codewars.com/kata/57a06005cf1fa5fbd5000216)
