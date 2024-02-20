#task1
pi = 3.14
degree = float(input("Enter a num: "))
rad = degree*(pi/180)
print(rad)

# Enter a num: 15
# 0.2616666666666667

#task 2

a = float(input("Enter one base: "))
b = float(input("Enter 2 base: "))
h = float(input("Enter height: "))
area = (a+b)/2 *h
print(area)

#Enter one base: 5
#Enter 2 base: 6
#Enter height: 5
#27.5

#task 3
from math import tan, pi
n_sides = int(input("Input number of sides: "))
s_length = float(input("Input the length of a side: "))
p_area = n_sides * (s_length ** 2) / (4 * tan(pi / n_sides))
print("The area of the polygon is: ",p_area)

#Input number of sides: 4                                                                                      
#Input the length of a side: 25                                                                                
#The area of the polygon is:625

#task4
b = float(input("Enter a base: "))
h = float(input("Enter a height: "))
S = b *h
print(S)
#Enter a base: 5
#Enter a height: 6
#30.0