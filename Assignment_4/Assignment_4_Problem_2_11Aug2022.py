# Assignment-4: Map | Filter | Lambda
# Problem 2 : Find the way with Maps
# Write a Python program to triple all numbers of a given list of integers. Use Python map.

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

b_list=valid_number_list()

m=list(map(lambda x:int(x)*3,b_list))

print("Result list with triple values of the entered numbers is :", m)

