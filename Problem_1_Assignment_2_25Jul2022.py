# Assignment - 2: List | Tuples | Dictionaries
# Problem 1 : Fun with Lists and Tuples 
# Write a Python program to get a list, sorted in increasing order by the last element 
# in each tuple from a given list of non-empty tuples 

list=[(2,5),(1,2),(4,4),(2,3),(2,1)]
print(list)
length=len(list)
j=0
k=0
smallest=0

for j in range (0,length):
    for k in range((j+1),(length)):
        if list[j][1]>list[k][1]:            
            smallest=list[k]
            list[k]=list[j]
            list[j]=smallest
print(list)

