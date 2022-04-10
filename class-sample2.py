from os import EX_USAGE

from importlib_metadata import email


class Employee:
    def __init__(self,ename,eage,esalary,erole):
        
        self.employeename = ename
        self.employeeage = eage
        self.employeesalary = esalary
        self.employeerole = erole
        self.email = self.employeename + '@snow.com'
        self.pension = True
        
emp1 = Employee("Venkatesh","45","50000","systems Admin")
emp2  = Employee("Arun","29","1000000","ceo")


print('{} {}'.format(emp1.email,emp2.email))




