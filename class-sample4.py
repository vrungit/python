## Inheritence in Class. employee class  gets inherited in other classes

class Employee:
    garden_leave = "2 months"
    def __init__(self,eid,efname,elname,eage,esal):
        self.employee_id = eid
        self.employee_fname = efname
        self.employee_lname = elname
        self.employee_age = eage
        self.employee_salary = esal
        self.employee_mail = self.employee_fname + self.employee_lname + '@snow.com'

class manager(Employee):
    def __init__(self, eid, efname, elname, eage, esal ):
        super().__init__(eid, efname, elname, eage, esal)
        self.car = True
        self.TravelBud = True
        self.House = True
        
class ic(Employee):
    def __init__(self, eid, efname, elname, eage, esal):
        super().__init__(eid, efname, elname, eage, esal)
        self.car = False
        self.TravelBud = True
        self.Oncall = True
        
class Director(Employee):
    

    def __init__(self, eid, efname, elname, eage, esal):
        super().__init__(eid, efname, elname, eage, esal)
        self.car = True
        self.TravelBud = True
        self.paidleave = True
    
        
        
emp1 = Director(100,"venk","moorthy",45,10000)
print(Director.garden_leave)
Director.garden_leave = "3 months"
print(Director.garden_leave)
print(emp1.garden_leave)