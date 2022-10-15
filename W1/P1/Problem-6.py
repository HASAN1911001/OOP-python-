"""
Write a Python program to print the first letter of your name using special character ‘*’.

Expected Output For H:
*       *
*       *
*       * 
* * * * *
*       *
*       *
*       *

"""
for row in range(7):
    for col in range(5):
        if col==0 or col==4:
            print("*", end=" ");
        elif row==3 and (col!=0 or col!=4):
            print("*", end=" ")
        else: print(" ", end=" ")
    print() 