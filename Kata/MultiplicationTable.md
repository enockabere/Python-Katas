## Python Multiplication Table Kata 1

### Description
Your goal is to return multiplication table for number that is always an integer from 1 to 10.

### Behavior Driven Development
The user should:
- input a string to see the multiplication table for that number
| Input |  Output    |
| ----- | ---------- |
| 5     | 1 * 5 = 5  |
|       | 2 * 5 = 10 |
|       | 3 * 5 = 15 |
|       | 4 * 5 = 20 |
|       | 5 * 5 = 25 |
|       | 6 * 5 = 30 |
|       | 7 * 5 = 35 |
|       | 8 * 5 = 40 |
|       | 9 * 5 = 45 |
|       | 10 * 5 = 50|

### Pseudocode
***define*** Function to perform multiplication of numbers
***set*** list range from 1 to 10
***input*** number
***loop** through the list multiplying the input
***return** String and Result

### Python Code

```text
#Check out this program
def mulTable():
    y = list(range(1,11))
    s =int(input("Enter number to check its multiples\n"))
    for x in y:
        z = x*s
        print(f"{x}*{s}={z}")
mulTable()
```
### Kata Link
[View Kata](https://www.codewars.com/kata/5a2fd38b55519ed98f0000ce).
