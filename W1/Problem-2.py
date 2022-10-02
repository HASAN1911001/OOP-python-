"""
Problem 2

Write a function that takes 3 integer inputs from user and
outputs absolute values of these integers without using any
library functions.

Sample Input:
-100
234
-350

Sample Output:
100
234
350


"""

a = input("Number: ")

if a[0] == '-':
    abs = a[1:]
else:
    abs = a[0:]
print(f'The absolute value of {a} is {abs}')