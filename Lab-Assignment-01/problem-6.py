""" -----------------------------------------------------------------------------------------------------

Complete the following code
def clean_string(text):
    ....
    ....
    print(output)
    
s = "P::::::,,,,,h;;;;i,,,t--r;,:o..N"

output = clean_string(s)
print(output)


If you face any errors, fix them. Get help from google. Do not ask others.

-------------------------------------------------------------------------------------------------------"""
import re

def clean_string(text):
    output = re.sub('[^A-Za-z0-9]+', '', text) 
    return output
    
s = "P::::::,,,,,h;;;;i,,,t--r;,:o..N"

output = clean_string(s)
print(output)