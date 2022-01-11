# calculator using python
a=int(input("Enetr the digit a \n"));
b=int(input("Enetr the digit b \n"));

i=int(input("Enter your choice for addition 1\nFor subtraction 2\nFor division 3\nFor multiplication 4\n"));

if i==1:
  c=int(a+b)
  print(c)  
elif i==2:
  c=a-b;
  print(c) 
elif i==3:
  c=a/b;
  print(c) 
elif i==4:
  c=int(a*b);
  print(c) 
else:
  print(("Enter your choice for addition 1\nFor subtraction 2\nFor division 3\nFor multiplication 4\n"));


