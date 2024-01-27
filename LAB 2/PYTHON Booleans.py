#TASK 1
print(10 > 9)

True

#TASK 2
print(10 == 9)

False

#TASK 3
print(10 < 9)

False

#TASK 4
print(bool("abc"))

True

#TASK 5
print(bool(0))

False

#EXAMPLE 1
print(10 > 9)
print(10 == 9)
print(10 < 9)

#EXAMPLE 2
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#EXAMPLE 3
print(bool("Hello"))
print(bool(15))

#EXAMPLE 4
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#EXAMPLE 5
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#EXAMPLE 6
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#EXAMPLE 7
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#EXAMPLE 8
def myFunction() :
  return True

print(myFunction())

#EXAMPLE 9
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

#EXAMPLE 10
x = 200
print(isinstance(x, int))