from re import A


class user:
    def __init__(self,uid,fname,lname,uage,ulocation,uheight,uweight):
        self.userid = uid
        self.firstname = fname
        self.lastname = lname
        self.age = uage
        self.location = ulocation
        self.height = uheight
        self.weight = uweight
    def bmi(self,uheight,uweight):
      
        return uheight * uweight
        
        

venki = user(100,"venkatesh","ramamoorthy",45,"uk",1.5,90)
print(venki.firstname)
print(venki.bmi())
