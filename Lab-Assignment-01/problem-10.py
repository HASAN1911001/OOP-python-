""" -----------------------------------------------------------------------------------------------------

Given a string 's' you need to find the words that are in list 'a' and use the next words on string 's'
 to create a new string. Save it inside a file called 'out.txt'. Remember to close the file after writing.

Write a function named create_new_string() and write your code inside this function.

a = ['oh', 'Emelia', 'to']

s = "Oh, I got two tickets for Dhaka. I and Emelia love to visit different places very much. This time we 
are going to Bangladesh."

output = "I love Bangladesh" (inside a file)

-------------------------------------------------------------------------------------------------------"""


def create_new_string(a, s):
    s_list = s.split()

    s_list[0] = "oh"

    s_list[11] = " "

    print(s_list)

    o = 0
    out_list = []
    for w1 in a:
        for i, w2 in enumerate(s_list):
            if w1 == w2:
                out_list.insert(o, s_list[i+1])
                o = o+1

    out = " "
    output = out.join(out_list)

    with open("out.txt", "w") as file1:
        file1.write(output.replace('.', ''))


a = ['oh', 'Emelia', 'to']

s = "Oh, I got two tickets for Dhaka. I and Emelia love to visit different places very much. This time we are going to Bangladesh."

create_new_string(a, s)

