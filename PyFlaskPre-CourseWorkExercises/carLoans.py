# Create a program in the Python shell that will calculate
# how long it would take a person to pay off a car loan of
# $150,000 if the person only spends 25% of his salary of $15,000
#  to pay the loan assuming no interest is charged.

def loanCalc():

    salary = 15000

    rate = (25*salary)//100

    loan = 150000

    repay = loan//rate

    print('-'*20)
    print('\n')
    print(f"Your loan of {loan} will be repayed in {repay} months")
loanCalc()
