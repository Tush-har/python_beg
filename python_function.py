# # function maximum of two number
# def max_two(x=0, y=1):
#   if(x>y):
#     return x;
#   else:
#      return y;

# # anothr fun.
# def max_three( x, y, z ):
#    return max_two( x, max_two( y, z ));

# c=max_three(2,15,7);
# print(c)

# sum of all the number in a list

# def sum(numbers):
#   total=0;
#   for x in numbers:
#     total=total+x;
#   return total;

# print(sum((1,2,3)))
  
def mult(num):
  i=1;
  for x in num:
    i*=x;
  return i;

print(mult((0,5,3)))
