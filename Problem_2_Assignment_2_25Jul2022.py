# Assignment - 2: List | Tuples | Dictionaries
# Problem 2 : Make Your Own mini-Dictionary 
# Write a Python program to print a dictionary whose keys should be the alphabet 
# from a-z and the value should be corresponding ASCII values

key_str="a"
ascii_num=ord(key_str)
my_dict={}
while chr(ascii_num)!="z":
    my_dict[chr(ascii_num)]=ascii_num
    ascii_num+=1
my_dict[chr(ascii_num)]=ascii_num
print(my_dict)


