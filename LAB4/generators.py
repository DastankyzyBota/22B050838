#task1
def generators_square(n):
    for i in range(n):
        yield i**2
    for x in generators_square(10):
        print(x)

#task2
def even_generator(a):
    i=0
    while i<=a:
        if i%2==0:
            yield i
        i+=1

n = int(input("Enter a num: "))
va = []
for i in even_generator(n):
    va.append(str(i))

print(",".join(va)) 

#Enter a num: 10
#0,2,4,6,8,10

#task3
def divisible(n):
    for i in range(n):
        if i % 3 ==0 and i%4 ==0 :
            print(str(i) + " ", end = "")
        else:
            pass


if __name__ == "__main__":

    n = 100
    
divisible(n)

#0 12 24 36 48 60 72 84 96 %       

#task4
square_gen = (i * i for i in range(6))
for i in square_gen:
    print(i)
# 0 1 4 9 16 25

#task5
import timeit

print timeit.timeit("range(10)[::-1]", number=10000000)
print timeit.timeit("range(9, -1, -1)", number=10000000)