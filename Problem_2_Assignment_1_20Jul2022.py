# Assignment - 1: Operators | Must Use Loops
# Write a Python program that accepts a word from the user and reverse it.
a=input("Enter Word ")
word_length = len(a)
print ("The reversed word is : ",end="")
i = -1
j = 1
while j <= word_length:
    print(a[i],end="")
    i=i-1
    j=j+1
print()

