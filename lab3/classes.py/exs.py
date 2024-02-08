#task1
class string:
    def init(a, string):
        a.string = string

    def getString(a):
        return a.string

    def printString(a):
        a.string = a.string.upper()
        return a.string

b = string(input())
c = b.getString()
print(c)
d = b.printString()
print(d)

#task2
class Shape:
    def init(self, length):
        self.length = length

    class Square:
        def init(self, side):
            self.side = side

    def area(self):
        return self.length*self.length


n = Shape(int(input()))
print(Shape.area(n))

#task3
class Rectangle:
    def init(self,width,length):
        self.width=width
        self.length=length
    def area(self):
        return self.length*self.width


n=Rectangle(int(input()),int(input()))
print(Rectangle.area(n))

#task4
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, self.y)

    def move(self, x1, y1):
        self.x = x1
        self.y = y1
        return Point(self.x, self.y)

    def dist(self):
        return math.sqrt((self.x)**2+(self.y)**2)


xy = Point(int(input()), int(input()))
Point.show(xy)

distance = Point.dist(xy)
print(distance)

xy = Point.move(xy, int(input()), int(input()))
Point.show(xy)

#task5
class Bank_account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self):
        print("Enter the sum you want to put in deposit:")
        money = float(input())
        self.balance += money
        return Bank_account(self.owner, self.balance)

    def withdraw(self):
        print("Enter the sum you want to take:")
        taken = float(input())
        while taken > self.balance:
            print("Enter the sum you want to take:")
            taken = float(input())
        self.balance -= taken
        return Bank_account(self.owner, self.balance)

    def __str__(self):
        return f"{self.owner} have {self.balance} money in his deposit."


account = Bank_account(input(), float(input()))
account = Bank_account.deposit(account)
account = Bank_account.withdraw(account)
print(account)

#task6
def filter_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


n = int(input())
l = []
for i in range(n):
    x = int(input())
    l.append(x)
primes = list(filter(filter_prime, l))
print(primes)