#TASK 1
i = 1
while i < 6:
    print(i)
    i += 1  

#TASK 2
i = 1
while i < 6:
    if i == 3:
        break
    i += 1

#TASK 3
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

#TASK 4
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")    

#EXAMPLE 1
i = 1
while i < 6:
  print(i)
  i += 1

#EXAMPLE 2
i = 1
while i < 6:
  print(i)
  if (i == 3):
    break
  i += 1

#EXAMPLE 3
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# Note that number 3 is missing in the result

#EXAMPLE 4
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")