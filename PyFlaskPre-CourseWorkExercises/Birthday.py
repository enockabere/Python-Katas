# Create a program where you prompt a user for
# their age and return the year they were born.

# After that, return the year they will turn 80.
import datetime
def birthday():

    now = datetime.datetime.now().year
    age = int(input("Enter Your age in Numbers\n"))
    yob = now-age
    ynext = 80-age

    print('\n')
    print(f"You were born on {yob}\n you will turn 80 on {ynext}")
birthday()
