#TASK 1
fruits = ("apple", "banana", "cherry")
print(fruits[0])

#TASK 2
fruits = ("apple", "banana", "cherry")
print(len(fruits))

#TASK 3
fruits = ("apple", "banana", "cherry")
print(fruits[-1])

#TASK 4
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])

#EXAMPLE 1
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#EXAMPLE 2
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#EXAMPLE 3
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#EXAMPLE 4
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#EXAMPLE 5
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

#EXAMPLE 6
tuple1 = ("abc", 34, True, 40, "male")

#EXAMPLE 7
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

#EXAMPLE 8
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

#EXAMPLE 9
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#EXAMPLE 10
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#EXAMPLE 11
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#EXAMPLE 12
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

#EXAMPLE 13
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

#EXAMPLE 14
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

#EXAMPLE 15
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

#EXAMPLE 16
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#EXAMPLE 17
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

#EXAMPLE 18
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

#EXAMPLE 19
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#EXAMPLE 20
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists\

#EXAMPLE 21
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#EXAMPLE 22
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

#EXAMPLE 23
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

#EXAMPLE 24
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#EXAMPLE 25
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

#EXAMPLE 26
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

#EXAMPLE 27
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#EXAMPLE 27
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)