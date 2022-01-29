#  BDD
'''
Expected user input
number of rows eg 3

Expected Output 

Print the number of stars
'''
# Pseudocode
'''
define a function to create a pattern
declare variable num to accept and store input

loop through the input as a range

append a star to a list multiplied my loop value

use join method to make the loop a string each in a new line.
'''

def pattern():
    num = int(input("Enter a number\t"))
    myList = []

    for i in range(1,num+1):
        myList.append('*'*i)
    print('\n'.join(myList))
pattern()
           
        