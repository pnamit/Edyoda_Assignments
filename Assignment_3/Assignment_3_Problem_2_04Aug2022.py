# Assignment 3 : Functions | Modules
# Problem 2 : String inside the function
# Write a Python program to reverse a string.


def reverse_string(input_string):
    """
    Accepts a string and returns the reverse
    """
    string_length=len(input_string)
    reverse_string_output=""
    for i in reversed(range(string_length)):
        reverse_string_output=reverse_string_output+input_string[i]
    #string_length=string_length-1
    return(reverse_string_output)    

a= input("Enter string : ")
print(reverse_string(a))


