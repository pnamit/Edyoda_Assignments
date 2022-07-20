# Assignment - 1: Operators | Must Use Loops
# Write a Python program to get the Fibonacci series between 0 to 50
a=0
b=1
c=1
print("The Fibonacci Series is : ", end="")
while c<50:
    print(c,end=",")
    c=a+b
    a=b
    b=c
print()

