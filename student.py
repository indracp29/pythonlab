class university:
    def __init__(self):
        stdid=age=marks=0

    def validmarks(self):
        if(self.marks>0 and self.marks<=100):
          return True
        else:
          return False

    def valid_age(self):
        if(age>=20):
            return True
        else:
            return False

    def qualification(self):
        if(self.validmarks() and self.valid_age()) :
            if(self.marks> 65):
                return True 
            else:
                return False
            
    def setter(self,sid,a,m):
        self.stdid=sid
        self.age=a
        self.marks=m

    def  getter(self):
         if(u1.qualification()):
          print("id",self.stdid)
          print("age",self.age)
          print("marks:",self.marks)
          print("given information is correct")
         else:
          print("not valid")


n=int(input("enter the no of students"))
for i in range(n):
        u1=university()
        stdid=int(input("enter the id"))
        age=int(input("enter the age"))
        marks=int(input("enter the marks"))
        u1.setter(stdid,age,marks )
        u1.getter()
                  


           
