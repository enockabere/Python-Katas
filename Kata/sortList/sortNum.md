# Python program to find smallest number in a list

## Description
Given a list of numbers, the task is to write a Python program to find the smallest number in given list.

## BDD


|       Given         |       Output          |
|---------------------|-----------------------|
|   [20,10,3,5,1,8]   | min = 1 and max = 20  |


## Pseudocode
- Define **function** to find min and max number in a list
- Declare  variable **x** to store values of a list
- use **min()** and **max()** iterable methods to get minimum and maximum values in **x** and store the in variable **y** and **z** respectively
- **Return** y and z

## Python code

```text
#sorting and referencing data at list locations
def sortNum():
    mylist = [7,20,1,2,3,4,5]
    
    sortList = sorted(mylist)
    
    print('Smallest Number = \t',sortList[0],'\n','Lagest Number = \t',sortList.pop())
sortNum()
#sorting and referencing data at list locations using pop() method
def sortNum():
    mylist = [7,20,1,2,3,4,5]
    
    sortList = sorted(mylist)
    
    print('Smallest Number = \t',sortList[0],'\n','Lagest Number = \t',sortList[-1])
sortNum()
#using min and max iterables to find smallest and largest integer
def sortNum():
    mylist = [7,20,1,2,3,4,5]
    
    print('Smallest Number = \t',min(mylist),'\n','Lagest Number = \t',max(mylist))
sortNum()
```
