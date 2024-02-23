#TASK 1
def squares1(n):
    for x in range(1, n + 1):
        if x * x > n:
            break
        yield x * x

# a = int(input())
# for x in squares1(a):
#     print(x)

#TASK 2
def even_num(num):
    even = (int(i) for i in range(0, num + 1, 2))
    for x in range(int(num / 2)):
        print(next(even), end = ", ")
    print(next(even))

# b = int(input())
# even_num(b)

#TASk 3
def divisible(n):
    for i in range(0, n + 1):
        if i % 12 == 0:
            yield i 
# c = int(input())
# for num in divisible(c):
#     print(num)

#TASK 4
def squares(a, b):
    sq = (int(i)**2 for i in range(a, b+1))
    for i in range (b - a + 1):
        print(next(sq))
        
# d = int(input())
# e = int(input())
# squares(d, e)

#TASK 5
def downto(n):
    while n >= 0:
        yield n
        n -= 1

# n = int(input())
# for num in downto(n):
#     print(num)