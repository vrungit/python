class Employee:
    def __init__(self,ename,eage,esalary,erole):
        
        self.employeename = ename
        self.employeeage = eage
        self.employeesalary = esalary
        self.employeerole = erole
        self.email = self.employeename + '@snow.com'
       
        
    def pension(self):
        print('{},{}'.format(self.employeename,self.employeesalary/12*2))
    
        
        
        
emp1 = Employee("Venkatesh","45",50000,"systems Admin")
emp2 = Employee("Arun","29",1000000,"ceo")

Employee.pension(emp1)
emp2.pension()