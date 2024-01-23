#EXAMPLE 1
print("Hello")
print('Hello')

#EXAMPLE 2
a = "Hello"
print(a)

#EXAMPLE 3
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#EXAMPLE 4
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#EXAMPLE 5
a = "Hello, World!"
print(a[1])

#EXAMPLE 6
for x in "banana":
  print(x)

#EXAMPLE 7
  a = "Hello, World!"
print(len(a))

#EXAMPLE 8
txt = "The best things in life are free!"
print("free" in txt)

#EXAMPLE 9
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#EXAMPLE 10
  txt = "The best things in life are free!"
print("expensive" not in txt)

#EXAMPLE 11
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

#EXAMPLE 12
  b = "Hello, World!"
print(b[2:5])

#EXAMPLE 13
b = "Hello, World!"
print(b[:5])

#EXAMPLE 14
b = "Hello, World!"
print(b[2:])

#EXAMPLE 15
b = "Hello, World!"
print(b[-5:-2])

#EXAMPLE 16
a = "Hello, World!"
print(a.upper())

#EXAMPLE 17
a = "Hello, World!"
print(a.lower())

#EXAMPLE 18
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
#EXAMPLE 19
a = "Hello, World!"
print(a.replace("H", "J"))

#EXAMPLE 20
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#EXAMPLE 21
a = "Hello"
b = "World"
c = a + b
print(c)

#EXAMPLE 22
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#EXAMPLE 23(WRONG)
age = 36
txt = "My name is John, I am " + age
print(txt)

#EXAMPLE 24
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#EXAMPLE 25
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#EXAMPLE 26
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

#EXAMPLE 27(WRONG)
# txt = "We are the so-called "Vikings" from the north."

#EXAMPLE 28
txt = "We are the so-called \"Vikings\" from the north."
