# #creating an object
# class PlayerCharacter:
#     def __init__(self,name):
#         self.name=name
#     def run(self):
#         print("run")
#
# player1=PlayerCharacter("tushar");
#
#
# print(player1)
# class Student:
#     pass
#
# tom=Student()
# zack=Student()
# tom.name="tommy"
# zack.name=["phy","hi"]
# tom.section="f"
# print(tom.name,zack.name)

class Employee:
    leaves=8;
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.role=arole
        self.salary=asalary
    def printdetails(self):
        return f"name is {self.name},salary is {self.salary},role is {self.role}"
tushar=Employee("tushar",777,"kkk");
# rohan=Employee();
# tushar.name="tushar"
# rohan.name="rohan"
# tushar.role="instr"
# rohan.role="student"
# tushar.salary=7877
# rohan.salary=855
# print(rohan.__dict__)
# rohan.leaves=7
# print(rohan.leaves)
# print(Employee.leaves)
# print(rohan.__dict__)
# print(rohan.printdetails())
# print(tushar.printdetails())
print(tushar.salary)
