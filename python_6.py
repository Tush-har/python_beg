# find dupk=licate values in list:
# some_list=['a','b','c','d','a','b','b','z'];
# new_list=[];
# for i in some_list:
#   if some_list.count(i)>1:
#     if i not in new_list:
#       new_list.append(i);

# # print(new_list)
# def say_hello():
#   print("helooo");

# say_hello()
# # print(say_hello)
# passing parameter(positional)
# def say_hello(idf,emoji):
#   print(idf,emoji)

# say_hello('helloooo','@')

# def say_hello(idf="null",emoji="null"):
#   print(idf,emoji)

# say_hello(idf='l',emoji='hii')
# say_hello()
# def sum(num1, num2):
#   def sum2(num1,num2):
#    return num1+num2;
#   return num1+num2;
#   # return this expression:!

# c=sum(4,5)
# print(c)
# print(sum(10,c))

# tesla problem udemy!

def checkDriverAge(age=0):
       age = input("What is your age?: ");
       if int(age)<18:
        print("Sorry, you are too young to drive this car. Powering off")
       elif int(age) > 18:
            print("Powering On. Enjoy the ride!");
       elif int(age) == 18:
          print("Congratulations on your first year of driving. Enjoy the ride!")

checkDriverAge(92)
