# Assignment 3 : Functions | Modules
# Problem 2 : Game of "Functions"
# Write a Python function to sum all the numbers in a list.



def valid_number_list():
    """
    Accepts only valid numbers from the user and returns them in a list
    """

    valid_numbers=[]
    b=0

    while b not in ("q","Q"):
        b=input("Enter a valid number (enter 'q' to quit) ")
        if b in ("q","Q"):
            break        
        elif b.isnumeric()==False:
            print("Entered number not valid. Please enter again")
        else:
            valid_numbers.append(b)
    return(valid_numbers)
    

def sum_list(input_list):
    """
    Accepts numbers in a list and returns the sum
    """
    sum=0
    for i in input_list:
        sum=sum+int(i)
    return sum

number_list=valid_number_list()
print(number_list)

sum_list(number_list)
print(sum_list(number_list))