'''---------------------------------------------------------------------------------
1. Create a function exp(a, n) that returns the exponential result ( a^n ). Read user 
input a and n in a single line from the keyboard.

Example input:
>> enter numbers: 2 3

Example Output:
>> result is: 8
-------------------------------------------------------------------------------------'''

def exp(a,n):
    exp = 1
    while(n):
        exp *= a
        n = n-1
    return exp

a, n = input("enter numbers: ").split()

a = int(a)
n = int(n)

print(f'result is: {exp(a, n)}')




