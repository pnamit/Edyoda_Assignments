# Assigment 3 : Functions | Modules
# Problem 3 : Calculate the Upper and The lower Case
# Write a Python function that accepts a string 
# and calculate the number of upper case letters and lower case letters.



def case_counter():
    """
    accepts a sentence and prints count of lower case and upper case alphabets
    """
    input_sentence = input(" Enter Sentence ")
    print("Entered Sentence :",input_sentence)

    sentence_length=len(input_sentence)
    upper_case_count=0
    lower_case_count=0

    for i in range(0,sentence_length):
        if (input_sentence[i].isupper())==True:
            upper_case_count+=1
        elif (input_sentence[i].islower())==True:
            lower_case_count+=1
        else:
            continue
    print("Number of upper case alphabets :",upper_case_count)
    print("Number of lower case alphabets :",lower_case_count)

case_counter()


