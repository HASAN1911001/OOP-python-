'''---------------------------------------------------------------------------------

2. Write a python to read three floating numbers from the keyboard in a single line with
'-' (dash) in between and output their sum.

Example input:
>> enter numbers: 2.3-4.5-1.7

Example Output:
>> sum is: 8.5

-------------------------------------------------------------------------------------'''

a, b, c = input("enter numbers: ").split("-")
a = float(a)
b = float(b)
c = float(c)

print(f'sum is: {a+b+c}')