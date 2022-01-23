
# # Public -
# # Protected -
# # Private -

# class Employee:
#     no_of_leaves = 8
#     var = 8
#     publickey=10
#     _protec = 9
#     __pr = 98

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

# emp = Employee("harry", 343, "Programmer")
# print(emp._Employee__pr)
# print(emp._protec)

# class A:
#     classvar1 = "I am a class variable in class A"
#     def __init__(self):
#         self.var1 = "I am inside class A's constructor"
#         self.classvar1 = "Instance var in class A"
#         self.special = "Special"

# class B(A):
#     classvar1 = "I am in class B"

#     def __init__(self):
#         self.var1 = "I am inside class B's constructor"
#         self.classvar1 = "Instance var in class B"
#         super().__init__()
#         # print(super().classvar1)
# class C(A):
#   def __init__(self):
#     self.special="Of class C"
#     self.var1="var 1 of class C"
#     super().__init__()
# Python program to demonstrate
# super function


# class Animals:
	
# 	# Initializing constructor
# 	def __init__(self):
# 		self.legs = 4
# 		self.domestic = True
# 		self.tail = True
# 		self.mammals = True
	
# 	def isMammal(self):
# 		if self.mammals:
# 			print("It is a mammal.")
	
# 	def isDomestic(self):
# 		if self.domestic:
# 			print("It is a domestic animal.")
	
# class Dogs(Animals):
# 	def __init__(self):
# 		super().__init__()

# 	def isMammal(self):
# 		super().isMammal()

# class Horses(Animals):
# 	def __init__(self):
# 		super().__init__()

# 	def hasTailandLegs(self):
# 		if self.tail and self.legs == 4:
# 			print("Has legs and tail")

# # Driver code
# Tom = Dogs()
# Tom.isMammal()
# Bruno = Horses()
# Bruno.hasTailandLegs()


# a = A()
# b = C()

# print(b.special, b.var1, b.classvar1)
# diamond problem
# class A:
#     def met(self):
#         print("This is a method from class A")

# class B(A):
#     # def met(self):
#     #     print("This is a method from class B")
#     pass

# class C(A):
#     def met(self):
#         print("This is a method from class C")

# class D(C, B):
#     # def met(self):
#     #     print("This is a method from class D")
#   pass

# a = A()
# b = B()
# c = C()
# d = D()

# d.met()
# print(dir(A))

# class Toy():
#   def __init__(self,color,age):
#     self.color=color
#     self.age=age
#     self.my_dict={
#         "name": "yoyo",
#         "pets": False
#     }


#   def __str__(self):
#     return f"{self.color}"

#   def __len__(self):
#     return 7

#   def __call__(self):
#     return ("yohhd")
  
#   def __getitem__(self,i):
#     return self.my_dict[i]





# action_figure=Toy("red",0)
# print(action_figure.__str__())
# print(str("action_figure"))
# print(len(action_figure))
# print(len("action_figure"))
# print(action_figure())
# print(action_figure["name"])
# class SuperList(list):
#   def __len__(self):
#     return 1000


# super_list1=SuperList();
# print(len(super_list1))
# super_list1.append(5)
# print(super_list1[0])
# print(issubclass(list,object))
# class A():
#     def __init__(self,age,weight):
#        self.weight=weight
#        self.age=age


#     def __add__(self,age,weight):
#            return (age,weight)
# class Employee:
#     def __init__(self):
#         self.name='Swati'
#         self.salary=10000
#     def __str__(self):
#         return 'name='+self.name+' salary=$'+str(self.salary)


# p=Employee()
# print(str(p))
