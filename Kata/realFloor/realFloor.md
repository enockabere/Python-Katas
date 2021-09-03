## Python What's the real floor Kata 2

### Description
Americans are odd people: in their buildings, the first floor is actually the ground floor and there is no 13th floor (due to superstition).

With the 1st floor being replaced by the ground floor and the 13th floor being removed, the numbers move down to take their place. In case of above 13, they move down by two because there are two omitted numbers below them.

### Behavior Driven Development
The user should:

    -Enter a floor number in the american system and the program returns the floor in the european system.

| Input   |  Output      |
| --------| --------|
|    0    |    1    |
|    0    |    0    |
|    4    |    4    |
|    13   |    15   |
|    -3   |    -3   |

### Pseudocode

> **Define** function to perform task

> **Input** floor number
> **If** floor number is equal to or greater than one and floor number is less or equal to 12
- **then** European floor number is equal to floor number minus one
- **return** European floor number
> **Else if** floor number is greater than 13
- **then** European floor number is equal to floor number minus 2
- **return** European floor number
> **Else if** floor number is equal to zero
- **return** European floor number is equal to zero
> **Else if** floor number is less than 0
- **return** European floor number is equal to European Floor Number
> **Else** return America doesn't have floor 13

### Python Code

```text
#Check out this program
def floor():
    floorNum = int(input("Enter floor number in American System\n"))
    if floorNum >= 1 and floorNum <=12:
        euroFlo0r = floorNum - 1
        print('-'*10)
        print('\n')
        print(f"Your Floor Number in Europe is {euroFlo0r}")
    elif floorNum >13:
        euroFlo0r = floorNum - 2 
        print('-'*10)
        print('\n')
        print(f"Your Floor Number in Europe is {euroFlo0r}")
    elif floorNum == 0:
        euroFlo0r = 0
        print('-'*10)
        print('\n')
        print(f"Your Floor Number in Europe is {euroFlo0r}")
    elif floorNum < 0:
        euroFlo0r = floorNum
        print('-'*10)
        print('\n')
        print(f"Your Floor Number in Europe is {euroFlo0r}")
    else:
        print('-'*10)
        print('\n')
        print("There is no 13th floor in America13")
floor()
```
### Kata Link
[View Kata](https://www.codewars.com/kata/574b3b1599d8f897470018f6).
