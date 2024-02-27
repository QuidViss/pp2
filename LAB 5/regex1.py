import re

#TASK 1
"""
a= input()
reg = re.search("a(b*)", a)
if reg:
   print("There is an 'a' followed by zero or more 'b''s")
else:
    print("There is no 'a' followed by zero or more 'b''s")
"""

#TASK 2
"""
b = input()
reg1 = re.search("(ab{2,3})", b)
if reg1:
   print("There is an 'a' followed by 2 or 3 'b''s")
else:
    print("There is no 'a' followed by 2 or 3 'b''s")
"""

#TASK 3
"""
c = input()
reg2 = re.findall("([a-z]_[a-z])+", c)
print(reg2)
"""

#TASK 4
"""
d = input()
reg3 = re.findall("([A-Z][a-z])+", d)
print(reg3)
"""

#TASK 5
"""
e = input()
reg4 = re.search("(.)*a(.)+b$", e)
if reg4:
    print("YES")
else:
    print("NO")
"""

#TASK 6 
"""
f = input()
reg5 = re.sub("[.,\\s]", ":", f)
print(reg5)
"""

#TASK 7
"""
g = input()
li = []
reg6 = re.split("_", g)
for x in reg6:
    li.append(x)
for y in li:
    print(y.capitalize() , end="")
"""

#TASK 8
"""
h = input()
reg7 = re.findall('[A-Z][^A-Z]*', h)
print(reg7)
"""

#TASK 9

# i = input()
# reg8 = re.sub(r"(\w)([A-Z])", r"\1 \2", i)
# print(reg8)


#TASK 10
"""
j = input()
reg9 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", j)
print(re.sub("([a-z0-9])([A-Z])", r"\1_\2", reg9).lower())
"""