print(type(2+4));
print(type(0.2-4));
print(2/4);
print(type('s'));
print(2**5);
print(2/4);
print(2//4);output=without decimal
print(abs(-3.9));//remove negative value
text formatting
print("hello {},your marks is {}.".format("tushar",100))
print("hello {0},your marks is {1}.".format("tushar",100))
print("hello {name},your marks is {marks}.".format(name="tushar",marks=100))
print("hello {0},your marks is {marks}.".format("tushar",marks=100))
c="a final match";
print(c[0]);
print(c[1]);
print(c[3]);
print(c[0]);

string manpulation
python="I am PYTHON";
print(python[1:4]);
print(python[1:]);
print(python[:]);
print(python[1:100]);
print(python[-1]);
print(python[-4]);
print(python[:-3]);
print(python[-3:]);
print(python[::-1]);
username=input("What is your username\n");
password=input("what  is your password\n");
password_length=len(password);
hidden_password='*'*password_length;
print(f'{username},your password\'s ,{hidden_password},is {password_length},letters long')
print(bin(1));
x='tushar';
x=x.capitalize()
print(x);
txt = "My nam|e is\ xxx"

x = txt.encode()

print(x)
list
cricket=['bat','ball','stumps',3];
print("\nItems Required to paly cricket\n")
cricket.append("xxx");
print(cricket);
create a dictinory
my_dict={
  'name': "tushar",
  'grad_year': '2nd',
  'course': 'Btech cse'
  'roll_number': 2000331530055

  

}
print(my_dict);
print(len(my_dict));
print(my_dict["name"])
print(my_dict["roll_number"])
print(list(my_dict.values()));
print(list(my_dict.items()));
print(list(my_dict.keys()))
print(my_dict.get('roll_number'))
new_dict=dict([['name','tushar'],['age',14]])
print(new_dict)
list
my_list=[1,2,3,'tushar','tushar',True];
x=len(my_list*2);
print(my_list*4)
print(my_list.count('tushar'));
print(my_list[0:3:2])
my_list.append(100)
print(my_list)
my_list.insert(0,"!!!")
print(my_list)
nc=my_list.copy()
print(nc)
print([1,2,3,4].reverse())

user={
  'basket': [1,2,3],
  'greert': 'hellooo'
}
user=dict(name='joghn')
print(user.get('name'));
print('sum of two integer\n');
print('enter a ');
x=int(input());
print(x)
y=int(input('enter data\n'))
x=int(input('enter datat\n'))
z=x+y;
print(z,"data");
disk={
  'album':'arijit singh',
  'song': [10,11,3],

}
x=disk.copy();
# disk.clear()
print(disk)

c=x.get('song')
print(x)
print(c)
print(x.setdefault('g',44))
print(x.get('g',44))
print(x.values('song'))
