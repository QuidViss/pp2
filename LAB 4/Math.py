import math
#TASK 1
def DegreeToRadian(deg):
    radian = float(deg / 57.272893)
    return radian

# a = int(input("Input degree: "))
# print("Output radian:", DegreeToRadian(a))

#TASK 2
def areaTrap(h, b1, b2):
    area = h * (b1 + b2) / 2
    return area

# height = int(input("Height: "))
# base1 = int(input("Base, first value: "))
# base2 = int(input("Base, second value: "))
# print("Expected Output:", areaTrap(height, base1, base2))

#TASK 3
def areaPolygon(n, l):
    area = (math.cos(math.pi / n) * (l ** 2) * n)/(math.sin(math.pi / n) * 4)
    return int(area)

# sides = int(input("Input number of sides: "))
# length = int(input("Input the length of a side: "))
# print("The area of the polygon is:", areaPolygon(sides, length))

#TASK 4
def areaParallelogram(lenb, hei):
    area = float(lenb * hei)
    return area

# lenb = int(input("Length of base: "))
# hei = int(input("Height of parallelogram: "))
# print("Expected Output:", areaParallelogram(lenb, hei))