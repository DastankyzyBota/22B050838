#1
def mult(nums):
    
     list = 1
     for i in nums:
        list = list * i
        return list

list1 = [1,2,3]
list2 = [5,6,7]
print(mult(list1))
print(mult(list2))
#6
#210

import numpy
list1 = [4,5,6]
list2 = [9,12,3]

res1 = numpy.prod(list1)
res2 = numpy.prod(list2)
print(res1)
print(res2)
#120
#324

#2
string = "GoodHealth"
low = 0
upp = 0
for i in string:
    if(i.islower()):
        low = low + 1
    else:
        upp = upp + 1
        print("The num of lower case:", low)
        print("The num of upper:", upp)

#3
def isPalindrome(string):
    revstr=''. join(reversed(string))
    if string==revstr:
        return "The string is a palindrome."
        return "The string is not a palindrome."

string = input ("Enter string: ")

#4
from time import sleep
import math
def milliseconds(f, g, *arg):
    sleep(g/1000)

    return f(*arg)
print("Sample Input: ")
print(milliseconds(lambda x: math.sqrt(x), 25100, 2123 ))
print(milliseconds(lambda x: math.sqrt(x), 1000, 100 ))
print(milliseconds(lambda x: math.sqrt(x), 2000, 25100 ))

#5
a = (True, True, False)
res = all(a)
print(res)