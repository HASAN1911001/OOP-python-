""" -----------------------------------------------------------------------------------------------------

Suppose you have a program that converts a string into Upper, Capitalized and Lower style using three different functions. Now create a test script for testing the three functionality of that program. Run using PyTest.

a. Write a function make_upper() to make the string in uppercase
b. Write a function make_capital() to make the string capitalized
c. Write a function make_lower() to make the string lowercase

Write a function named test_script() and write your code inside this function.

-------------------------------------------------------------------------------------------------------"""

def make_upper(str):
    return str.upper()

def make_lower(str):
    return str.lower()

def make_capital(str):
        return str.capitalize()
    #str_list = str.split()

    # if len(str_list) == 1:
    #     return str.capitalize()

    # for i, word in enumerate(str_list):
    #     str_list[i] = word.capitalize()
    
    # out = " "
    # return(out.join(str_list))

    

str = 'ziaul Hasan'

if __name__ == "__main__":
    print(make_upper(str))
    print(make_lower(str))
    print(make_capital(str))


