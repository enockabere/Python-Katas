# Create a program that lets the user input their total bill at a restaurant,
# and returns the total cost of the bill including a tip. let the user enter
# their level of satisfaction with their service and factor that value into the tip percentage.
# For example, if they received good service, the tip is 15%; great service is 20%; terrible service is 0%.

def tipCalc():
    bill= int(input("Enter your total bill\n"))
    satisfaction = int(input ("What is your level of satisfaction answer with 1= good, 2=great, 3=poor\n"))

    if satisfaction == 1:
        tip = (15*bill)//100
        totalBill = tip + bill
        print('\n')
        print(f"Total bill including tip is{totalBill}")
    elif satisfaction == 2:
        tip = (25*bill)//100
        totalBill = tip + bill
        print('\n')
        print(f"Total bill including tip is{totalBill}")
    elif satisfaction == 3:
        totalBill = bill
        print('\n')
        print(f" Sorry for the poor service your Total bill is{totalBill}")
    else:
        print('\n')
        print("Invalid Entry")
tipCalc()
        
