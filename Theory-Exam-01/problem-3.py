'''---------------------------------------------------------------------------------
3. Write a python program to reverse every word from a given string s and output a new string. 
The position of words will remain the same, but their contents will be in reverse order.

s = “Programming Hero is the best”

Expected output: “gnimmargorP oreH si eht tseb”

-------------------------------------------------------------------------------------'''

s = input("input: ").split()

for i, w in enumerate(s):
    s[i] = w[::-1]

output = " ".join(s)
print(f'Output: {output}')

