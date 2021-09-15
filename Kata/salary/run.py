class Payroll:
    def __init__(self,basic_salary):
        self.basic_salary = basic_salary
    def payee(self):
        if self.basic_salary > 1 and self.basic_salary <= 24000:
           rate = 0.1 
           salary = self.basic_salary*rate 
        print("Your Payee is :-", salary)
        
gross = int(input("Enter your basic salary\n"))
salary = Payroll(gross)
salary.payee()
        
    