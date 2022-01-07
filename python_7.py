# def test(a):
#   '''
#   info: this function is useless
#   '''
#   print(a);

# test('!!!!!')
# help(test)
# print(test.__doc__);
# def super_fun(*arg,**kwarg):
#   print(arg)
#   print(kwarg)
# # print(super_fun(1,2,3,4,5))
# (super_fun(1,2,3,4,5, num1=5,num2=10))
# print("The items are\n");
# super_fun(1,2,3);

# def highest_even(li):
#   evens=[];
  
#   for i in li:
#     if i%2==0:
#       evens.append(i);

#   return max (evens)
    



# print(highest_even([10,2,3,4,8,11])) 
# walure 
a="helloooooooooo"

if((n := len(a)) > 10):
  print(f"too long {n} elements")

  while((n := len(a))>1):
    print(n)
    a=a[:-1]
  
  print(a)
