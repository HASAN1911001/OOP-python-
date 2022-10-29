'''---------------------------------------------------------------------------------
4. Write a python program for the requirement below. Notice the output must be in sorted order -
Input  : x3b4U5i2
Output : bbbbiiUUUUUxxx

-------------------------------------------------------------------------------------'''

s = input("Input: ")

s_list = list(s)

u_list = []
j = 0

for i, c in enumerate(s_list):
    if i%2 == 0:
        u_list.append(c)
    else:
        c = int(c)
        while(c-1):
            u_list.append(s_list[i-1])
            c = c-1

u_list = sorted(u_list, key=lambda L: (L.lower(), L))
output = "".join(u_list)
print(f'Output: {output}')
    

    


