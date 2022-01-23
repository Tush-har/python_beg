# class Vehicle():
#     def __init__(self,model,max_speed,mileage):
#       self.model=model
#       self.max_speed=max_speed
#       self.mileage=mileage

# class Bus(Vehicle):
#   pass
  


# honda=Vehicle("Honda",47,75)
# c=str(honda.mileage)
# d=str(honda.max_speed)
# e=str(honda.model)
# print("The model of bike is " +e+"\nwhose maximum speed is "+d +"\nand mileage is "+c)

# r=Bus("Red bus and sr",140,100)
# u=str(r.max_speed)
# s=str(r.model)
# b=str(r.mileage)
# print("The model of Bus is " +s+"\nwhose maximum speed is "+u +"\nand mileage is "+b)


# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

#     def seating_capacity(self, capacity=50):
          
#         return f"The seating capacity of a {self.name} is {capacity} passengers"

# class Bus(Vehicle):
#   pass

# bus=Bus("Baba bus sr.",220,100)
# # print(bus.seating_capacity())
# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity

#     def fare(self):
#         return self.capacity * 100

# class Bus(Vehicle):
#     pass

# School_bus = Bus("School Volvo", 12, 50)
# print("Total Bus fare is:", School_bus.fare())
# print(type(School_bus))
# print(isinstance(School_bus, Vehicle))
# class Rectangle():
#     def __init__(self,length,width):
# #       self.length=length
# #       self.width=width
# #     def paremeter(self):
# #       return 2*(self.length+self.width)
    
# #     def area(self):
# #       return self.length*self.width;
    

# # r=Rectangle(7,5);
# # print(r.area()) 
# # print(r.paremeter()) 

# class Person():
#       def __init__(self,name,age):
#         self.name=name;
#         self.age=age;

#       def dispaly(self):
#         print("Person name",self.name);
#         print("Person age",self.age);

# def Child(Person):
#       def __init__(self, name , age , section):
#         Person.__init__(self,name,age)
#         self.section=section;
      
#       def dispaly_student(self):
#           print("student name",self.name);
#           print("student age",self.age);
#           print("student section",self.section);

# # P = Person("Tomas Wild", 37)
# # P.display()
# print("-------------------------------")
# S = Child("Albert", 23 , "Mathematics")
# # S.display()
# class Person:
#     # define constructor with name and age as parameters
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     # create display method fro Person class
#     def display(self):
#         print("Person name : ", self.name)
#         print("Person age = ", self.age)
    
# # create child class Student of Person class
# class Student(Person):
#     # define constructor of Student class with section additional parameters 
#     def __init__(self, name , age , section):
#         Person.__init__(self,name, age)
#         self.section = section
    
#     # Create display method for Student class
#     def displayStudent(self):
#         print("Student name : ", self.name)
#         print("Student age = ", self.age)
#         print("Student section = ", self.section)
    
# # Testing Person class
# P = Person("Tomas Wild", 37)
# P.display()
# print("-------------------------------")
# S = Student("Albert", 23 , "Mathematics")
# S.displayStudent()


# class Employee:
#     no_of_leaves = 8
#     var = 8

#     def __init__(self, aname, asalary, arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole

#     def printdetails(self):
#         return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

#     @classmethod
#     def change_leaves(cls, newleaves):
#         cls.no_of_leaves = newleaves

#     @classmethod
#     def from_dash(cls, string):
#         return cls(*string.split("-"))

#     @staticmethod
#     def printgood(string):
#         print("This is good " + string)

# class Player:
#     var = 9
#     no_of_games = 4
#     def __init__(self, name, game):
#         self.name = name
#         self.game =game

#     def printdetails(self):
#         return f"The Name is {self.name}. Game is {self.game}"

# class CoolProgramer(Player, Employee):

#     language = "C++"
#     def printlanguage(self):
#         print(self.language)

# harry = Employee("Harry", 255, "Instructor")
# rohan = Employee("Rohan", 455, "Student")

# shubham = Player("Shubham", ["Cricket"])
# karan = CoolProgramer("Karan",["Cricket"])
# det = karan.printdetails()
# karan.printlanguage()
# print(det)
# print(karan.var)

class Employee():
    holiday=10
    def __init__(self,name,age):
      self.name=name 
      self.age=age

    def printdetail(self):
        return f"The Name is {self.name}. age is {self.age}"

class Skill():
    holiday=12
    def __init__(self,name,skills):
      self.name=name
      self.skills=skills

    def printdetail(self):
      return f"The Name is{self.name},skills are {self.skills}"

class CoolEmployee(Employee,Skill):
     
     print("This is a cool boy\n")

tushar=CoolEmployee("Tushar",12);
print(tushar.printdetail())
print(tushar.holiday)

