#TASK 1
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

#TASK 2
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"

#TASK 3
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

#TASK 4
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")

#TASK 5
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

#TASK 6
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

#TASK 7
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

#TASK 8
fruits = ["apple", "banana", "cherry"]
print(len(fruits))

#EXAMPLE 1
thislist = ["apple", "banana", "cherry"]
print(thislist)

#EXAMPLE 2
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#EXAMPLE 3
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#EXAMPLE 4
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#EXAMPLE 5
list1 = ["abc", 34, True, 40, "male"]

#EXAMPLE 6
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#EXAMPLE 7
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#EXAMPLE 8
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#EXAMPLE 9
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#EXAMPLE 10
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#EXAMPLE 11
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#EXAMPLE 12
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#EXAMPLE 13
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#EXAMPLE 14
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#EXAMPLE 15
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#EXAMPLE 16
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#EXAMPLE 17
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#EXAMPLE 18
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#EXAMPLE 19
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
#EXAMPLE 20
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#EXAMPLE 21
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#EXAMPLE 22
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#EXAMPLE 23
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#EXAMPLE 24
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#EXAMPLE 25
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#EXAMPLE 26
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#EXAMPLE 27
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#EXAMPLE 28
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#EXAMPLE 29
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#EXAMPLE 30
thislist = ["apple", "banana", "cherry"]
del thislist

#EXAMPLE 31
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#EXAMPLE 32
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#EXAMPLE 33
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#EXAMPLE 34
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#EXAMPLE 35
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#EXAMPLE 36
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#EXAMPLE 37
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

#EXAMPLE 38
ruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]

#EXAMPLE 39
ruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]

#EXAMPLE 40
newlist = [x for x in range(10)]

#EXAMPLE 41
newlist = [x for x in range(10) if x < 5]

#EXAMPLE 42
ruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]

#EXAMPLE 43
ruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]

#EXAMPLE 44
ruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]

#EXAMPLE 45
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#EXAMPLE 46
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#EXAMPLE 47
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#EXAMPLE 48
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#EXAMPLE 49
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#EXAMPLE 50
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#EXAMPLE 51
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#EXAMPLE 52
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#EXAMPLE 53
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#EXAMPLE 54
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#EXAMPLE 55
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#EXAMPLE 56
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

#EXAMPLE 57
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)