#task1
def ounces_to_grams(weight):
    new_weight = weight * 28.3495
    return new_weight

weight_in_grams = 999

weight_in_ounce = ounces_to_grams(weight_in_grams)

print(f"{weight_in_ounce} oun")
#28321.1505 oun

#task2
def f_to_c(temperature):
    new_temp = (5/9)*(temperature - 32)
    return new_temp

temp_in_F = 565

temp_in_C = f_to_c(temp_in_F)

print(f"{temp_in_C} f")
#296.11111111111114 f

#task3
def solve(heads, legs):
    error= "no sol"
    chickens = 0
    rabbits=0

    if(heads>=legs):
        print(error)
    elif(legs%2 !=0):
        print(error)
    else:
        rabbits = (legs - 2*heads)/2
        chickens = heads - rabbits
        print(int(chickens), int(rabbits))



solve(35,94)      
#23 12

#task4
import math
def filter_prime(x):
    s =1
    for i in range(2,int(math.sqrt(x))+1):
        if(x%i==0):
            s=0
            print("Not Prime")
            break
        else:
            continue
        if(s==1):
            print("Prime num")
            return s



num = int(input("Nums: "))
res = filter_prime(num)

#task5
a ='abc'

def permutation(str, ba=0):

    if ba == len(str)-1:
        print("".join(str))

    for c in range(ba, len(str)):
        word = [d for d in str]
        word[ba], word[c] = word[c], word[ba]

        permutation(word, ba+1)

new_permutation = permutation(a)
print(new_permutation)
#abc
#acb
# bac
# bca
# cba
# cab

#task6
a = input()
a = a.split()[::-1]
b = list()
for i in a:
    b.append(i)
    print(" ".join(b))

#task7
def has__33(nums):
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1] == 3:
            return True
    return False


a = list()
b = int(input())
for i in range(b):
    x = int(input())
    a.append(x)
print(has__33(a))

#task8 
def spygame(nums):
    for i in range(len(nums)-2):
        if nums[i] == nums[i+1]==0 and nums[i+2]==7:
            return True
            return False

    a = int(input())
    b = list()
    for i in range(a):
        x = int(input())
        b.append(x)
        print(spygame(b))

#task 9 
def Volume_Sphere(radius : float):
    a = (4/3) * 3.14
    b = radius ** 3
    V = a*b
    return V

    print("Radius: ")
    c = int(input())
    d = Volume_Sphere(c)
    print("Volume: ", d)

    #task 10
    def unique_lst(a):
        b = []
        for i in a:
            if i not in b:
                b.append(i)
                return b


    d = int(input())
    a = list()
    for j in range(d):
        b = int(input())
        a.append(b)
        print(unique_lst(a))

        #task11
        def isPalindrome(string):
          left_pos = 0
          right_pos = len(string) - 1
          while right_pos >= left_pos:
            if not string[left_pos] == string[right_pos]:
                return False
                left_pos += 1
                right_pos -= 1
                return True
                s = input()
                print(isPalindrome(s)) 

                #task12
                def histogram(items):
                    for n in items:
                        output = ''
                        times = n
        while( times > 0 ):
            output += '*'
            times = times - 1
        print(output)
        n=int(input())
        l=[]
        for i in range(n):
            x=int(input())
            l.append(x)
    print(histogram(l))

# task13
import random

number = random.randint(1, 20)
tries = 1
print("Hello! What is your name?")
name = input()
print(f"Well, {name}, I am thinking of a number between 1 and 20.")
g = "Take a guess."
print(g)
n = int(input())
while (n != number):
    if (n < number):
        print("Your guess is too low.")
    elif (n > number):
        print("Your guess is too high.")
    print(g)
    tries += 1
    n = int(input())

print(f"Good job, {name}! You guessed my number in {tries} guesses!")
