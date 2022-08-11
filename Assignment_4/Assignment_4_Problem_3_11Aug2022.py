# Assignment-4: Map | Filter | Lambda
# Problem 3 : Find the Squares from the given List
# Write a Python program to square the elements of a list using map() function.

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
            print("Invalid entry")
        else:
            valid_numbers.append(b)
    return(valid_numbers)


b_list=valid_number_list()
m=list(map(lambda x:int(x)**2,b_list))
print("The squares of the entered numbers are :",  m)

