# Assignment - 1: Operators | Must Use Loops
# Write a Python program to count the number of even and odd numbers from a series of numbers.
number_list = [1,2,3,4,5,6,7,8,9]
print("List of numbers : ",number_list)
length=len(number_list)

even_count = 0
odd_count = 0
j=0

while j <length:
    if (number_list[j])%2==0:
        even_count+=1
    else:
        odd_count+=1
    j+=1
print("Number of Even Numbers = ",even_count)
print("Number of Odd Numbers = ",odd_count)

