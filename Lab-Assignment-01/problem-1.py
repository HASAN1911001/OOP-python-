""" -----------------------------------------------------------------------------------------------------

Create a string out of some words given in a list -

l = ["This", "is", "very", "fantastic"]


Expected Output:
"This is very fantastic"

Write a function named create_string() and write your code inside this function.

-------------------------------------------------------------------------------------------------------"""

def create_string(l):
   
    # initialize an empty string
    str1 = " "
   
    # return string 
    return (str1.join(l))
       
       
# Driver code   
l = ["This", "is", "very", "fantastic"]
print(create_string(l))