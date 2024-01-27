#TASK 1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")

#TASK 2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

#TASK 3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

#TASK 4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

#TASK 5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")

#EXAMPLE 1
thisset = {"apple", "banana", "cherry"}
print(thisset)

#EXAMPLE 2
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

#EXAMPLE 3
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

#EXAMPLE 4
thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

#EXAMPLE 5
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

#EXAMPLE 6
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

#EXAMPLE 7
set1 = {"abc", 34, True, 40, "male"}

#EXAMPLE 8
myset = {"apple", "banana", "cherry"}
print(type(myset))

#EXAMPLE 9
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

#EXAMPLE 10
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#EXAMPLE 11
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

#EXAMPLE 12
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#EXAMPLE 13
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#EXAMPLE 14
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

#EXAMPLE 15
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

#EXAMPLE 16
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

#EXAMPLE 17
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

#EXAMPLE 18
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

#EXAMPLE 19
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)

#EXAMPLE 20
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#EXAMPLE 21
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#EXAMPLE 22
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#EXAMPLE 23
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

#EXAMPLE 24
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

#EXAMPLE 25
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

#EXAMPLE 26
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)

#EXAMPLE 27
x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}

z = x.symmetric_difference(y)

print(z)