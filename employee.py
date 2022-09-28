"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Commission:
    def __init__(self):
        pass

    def get_com(self):
        pass

    def __str__(self):
        pass

class FixedCommission(Commission):
    def __init__(self, fixed):
        self.fixed = fixed

    def get_com(self):
        return self.fixed

    def __str__(self):
        return " and receives a bonus commission of {0}.".format(self.fixed)

class ContractCommission(Commission):
    def __init__(self, contracts_landed, pay_per_contract):
        self.contracts_landed = contracts_landed
        self.pay_per_contract = pay_per_contract

    def get_com(self):
        return self.contracts_landed * self.pay_per_contract

    def __str__(self):
        return " and receives a commission for {0} contract(s) at {1}/contract.".format(self.contracts_landed, self.pay_per_contract)

class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        pass

    def total_pay_str(self):
        return "Their total pay is {0}.".format(self.get_pay())

    def __str__(self):
        return self.name

class MonthlyEmployee(Employee):
    def __init__(self, name, monthly_pay, com=None):
        super().__init__(name)
        self.monthly_pay = monthly_pay
        self.com = com

    def get_pay(self):
        com_pay = 0 if self.com == None else self.com.get_com()
        return self.monthly_pay + com_pay

    def __str__(self):
        com_str = str(self.com) if self.com != None else "."
        pay_str = "{0} works on a monthly salary of {1}{2}  {3}".format(self.name, self.monthly_pay, com_str, self.total_pay_str())

        return pay_str

class HourlyEmployee(Employee):
    def __init__(self, name, hourly_pay, hours_worked, com=None):
        super().__init__(name)
        self.hourly_pay = hourly_pay
        self.hours_worked = hours_worked
        self.com = com

    def get_pay(self):
        com_pay = 0 if self.com == None else self.com.get_com()
        return self.hourly_pay * self.hours_worked + com_pay

    def __str__(self):
        com_str = str(self.com) if self.com != None else "."
        pay_str = "{0} works on a contract of {1} hours at {2}/hour{3}  {4}".format(self.name, self.hours_worked, self.hourly_pay, com_str, self.total_pay_str())

        return pay_str

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
# billie = Employee('Billie')
billie = MonthlyEmployee("Billie", 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = HourlyEmployee('Charlie', 25, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = MonthlyEmployee('Renee', 3000, ContractCommission(4, 200))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = HourlyEmployee('Jan', 25, 150, ContractCommission(3, 220))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = MonthlyEmployee('Robbie', 2000, FixedCommission(1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = HourlyEmployee('Ariel', 30, 120, FixedCommission(600))
