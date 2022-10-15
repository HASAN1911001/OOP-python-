""" -----------------------------------------------------------------------------------------------------

x = { 'a' : 1, 'b' :  2, 'c': 3, 'd': 4}
output:  [ 'a', 1, 'b',  2, 'c', 3, 'd', 4]


Now do the same for -
d = {'!': 1, '@' : 2, '#': 3, '$' : 4, '%' : 5, '^' : 6}


Write a function named create_list() and write your code inside this function.

-------------------------------------------------------------------------------------------------------"""

def create_list(dict):
    li = []

    for i in dict:
        li.append(i)
        li.append(dict[i])
    
    return li

d = {'!': 1, '@' : 2, '#': 3, '$' : 4, '%' : 5, '^' : 6}

li = create_list(d)

print(li)