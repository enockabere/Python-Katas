# Create a program in the Python shell that allows
# you to calculate the body mass index of the person.
# This is calculated by dividing a person's weight by
# their height in meters squared.

def bmi_calc():

    weight= int(input("What is your weight in Kgs \n"))

    height = int(input("What is your height in (FT) \n"))

    converter = 720.305

    bmi = weight/((height*converter)**2)

    print ('-'*10)
    print('\n')
    print(f"Your BMI index is {bmi}")
bmi_calc()
