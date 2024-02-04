from itertools import permutations
import math
import random

"""
IN ALL EXERCISES BELOW I HAVE COMMENTED THE OUTPUT 
"""

#TASK 1
def func(grams):
    ounces = 28.3495231 * grams
    print(ounces)

# grams = int(input()) 
# func(grams)

#TASK 2
def Fahreheit_To_Centigrade(F):
    C = float((5 / 9) * (F - 32))
    print(C)

# F = int(input())
# Fahreheit_To_Centigrade(F)

#TASK 3
def Number_of_chickens_and_rabbits(heads,legs):
    rabbit_count = (legs - 2 * heads) / 2
    chicken_count = heads - rabbit_count
    print(int(chicken_count),int(rabbit_count))
heads = 35
legs = 94

# Number_of_chickens_and_rabbits(heads, legs)

#TASK 4
def only_primes(a):
    x = 1
    for i in range(2, a):
        if(a % i ==0 ):
            x = 0
    if(x == 1):
        print(a, end = " ")

# list1 = input().split()
# for i in range(len(list1)):
#    only_primes(int(list1[i]))
# print()

#TASK 5
def all_permutations(s):
    numes = list()
    for a in s:
        numes.append(a)
    permutationss = list(permutations(numes))
    for permutation in permutationss:
        print(''.join(permutation))
        
# s = input()
# all_permutations(s)

#TASK 6
def rever(s):
    x = s.split()
    x.reverse()
    for i in x:
        print(i, end=" ")


# s1 = "WE AsdF DSFFDSfs"
# rever(s1)

#TASK 7
def has_33(a):
    last = -1
    for x in a:
        if last == 3 and x == 3:
            return True
        else: last = x
    return False

# print(has_33([1, 3, 3]))
# print(has_33([1, 3, 1, 3]))
# print(has_33([3, 1, 3]))

#TASK 8
def spy_game(nums):
    arr = [7, 0, 0]
    for x in nums:
        if arr[-1] == x:
            arr.pop()
        if len(arr) == 0:
            return True
    return False

# print(spy_game([1,2,4,0,0,7,5]))
# print(spy_game([1,0,2,4,0,5,7]))
# print(spy_game([1,7,2,0,4,5,0]))

#TASK 9

def volume(radius):
    vol = float(4/3 * math.pi * (radius ** 3))
    print(vol)
    
# radius = float(input())
# volume(radius)

#TASK 10
def unique_(list):
    uniq = []
    for elem in list:
        if elem not in uniq:
            uniq.append(elem)
    return uniq

# list = [1, 2, 2, 3, 4, 4, 5]
# print(unique_(list))

#TASK 11
def is_palindrome(word):
    return word == word[::-1]

# word1= "mom"
# word2= "moma"
# print(is_palindrome(word1))
# print(is_palindrome(word2))

#TASK 12
def histogram(numba):
    for qwerty in numba:
        print('*' * qwerty)

# print(histogram([4, 9, 7]))

#TASK 13

def guess_the_number():
    name = input("Hello! What is your name?\n")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    number = random.randint(1, 20)
    attempts = 0
    while True:
        print("Take a guess.")
        guess = int(input())
        attempts += 1

        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {attempts} guesses!")
            break

# guess_the_number()