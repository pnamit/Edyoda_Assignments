# Assignment-5: OOPS
# Problem 1 : Create You own built-in class method
# Write a Python class to implement pow(x, n)
# You must implement it using Class

class Math_functions:
    def __init__(self):
        pass

    def accept_user_input_number(self):  
        val_number='a'
        while val_number.isnumeric()==False: 
            val_number=input(f"Enter a valid number for the {self.number_type} : ")
            if val_number.isnumeric()==True:
                break
            else:
                print("Invalid entry")    
        return(val_number)
    
    def calc_exponential_value(self,base,exponent):
        self.base=base
        self.exponent=exponent
        return(base**exponent)

x=Math_functions()

x.number_type="Base (b)"
b=int(x.accept_user_input_number())

x.number_type="Exponent (e)"
e=int(x.accept_user_input_number())

print(f"Result (b to the power of e) : {x.calc_exponential_value(b,e)}")






