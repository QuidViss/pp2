#TASK 1
carname = "Volvo"

#TASK 2
x = 50

#TASK 3
x = 5
y = 10
print(x + y)

#TASK 4
x = 5
y =10
z = x + y
print(z)

#TASK 5
x, y, z = "Orange", "Banana", "Cherry"

#TASK 6
x = y = z = "Orange"

#TASK 7
def myfunc():
	global x
	x = "fantastic"

#EXAMPLE 1
x = 5
y = "John"
print(x)
print(y)

#EXAMPLE 2
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#EXAMPLE 3
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#EXAMPLE 4
x = 5
y = "John"
print(type(x))
print(type(y))

#EXAMPLE 5
x = "John"
# is the same as
x = 'John'

#EXAMPLE 6
a = 4
A = "Sally"
#A will not overwrite a

#EXAMPLE 7
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#EXAMPLE 8(WRONG)
# 2myvar = "John"
# my-var = "John"
# my var = "John"

#EXAMPLE 9
myVariableName = "John"

#EXAMPLE 10
MyVariableName = "John"

#EXAMPLE 11
my_variable_name = "John"

#EXAMPLE 12
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#EXAMPLE 13
x = y = z = "Orange"
print(x)
print(y)
print(z)

#EXAMPLE 14
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#EXAMPLE 15
x = "Python is awesome"
print(x)

#EXAMPLE 16
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#EXAMPLE 17
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#EXAMPLE 18
x = 5
y = 10
print(x + y)

#EXAMPLE 19(WRONG)
x = 5
y = "John"
print(x + y)

#EXAMPLE 20
x = 5
y = "John"
print(x, y)

#EXAMPLE 21
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#EXAMPLE 22
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#EXAMPLE 23
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#EXAMPLE 24
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)