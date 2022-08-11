# Assignment-4: Map | Filter | Lambda
# Problem 1 : Play with Lambda
# Write a Python program to create a lambda function 
# that adds 25 to a given number passed in as an argument.

def valid_number():
    """
    Accepts a valid number from the user and returns it
    """
    val_number='a'
    while val_number.isnumeric()==False: 
        val_number=input("Enter a valid number :")
        if val_number.isnumeric()==True:
            break
        else:
            print("Invalid entry")
    
    return(val_number)

b=int(valid_number())
#print(b)

x=lambda a: a+25
print("The result after adding 25 is", x(b))

