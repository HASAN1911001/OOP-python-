"""
Problem 4

Write a Python program to check if user entered number is ZERO, POSITIVE or
NEGATIVE until user does not want to quit.
User will type ‘Quit’ to close the program.
Sample:
> Enter input: 2
> 2 is positive
> -3
> -3 is negative
> “Quit”
> (stop the program)
"""

while(1):
    a = input("Enter the number: ")

    if a[0] == '-': print(f'{a} is Negative')
    elif a[0] == '0': print(f'{a} is Zero')
    elif a == "Quit": break
    else: print(f'{a} is Positive')
