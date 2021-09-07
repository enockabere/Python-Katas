# Py Code to Reverse a Sentence and Characters
## Description
Complete the solution so that it reverses all of the words within the string passed in.
## BDD
To reverse a sentence one should:

  -Input a sentence to reverse

|             Input           |        Output        |
|-----------------------------|----------------------|
| Str eg = Hypertext Assassin | Assassin Hypertext   |

To reverse characters in a string one should:

    -Input a string to reverse

|       Input        |  Output     |
|--------------------|-------------|
| Str eg = Hypertext | txeterpyH   |

## Pseudocode
- Define function to reverse a string
- Declare a variable to accept input and store an string
- If condition to check whether string entered is a sentence
- If sentence then split, join and reverse string
- Output reversed string
- Else return invalid string
## Python code
```text
def reverse_string():
    print("-"*5,'We\'re about to reverse a string','-'*5,'\n')
    
    '''
    declare a variable to store a string to be reversed
    and split the string into words
    '''
    
    mystring = input("Enter Sentence to Reverse\n")
    
    #check whether string entered is a sentence
    if ' ' in mystring:
        correct = mystring.split(' ')
    
        #reverse and join using space    
        mystring_reverse = ' '.join(reversed(correct))
    
        print ('*'*2,'Reversed String','*'*2,'\n',mystring_reverse)
    else:
        print("Invalid string! It should be a sentence")
reverse_string()
```
## Kata link
[viewkata](https://www.codewars.com/kata/51c8991dee245d7ddf00000e)