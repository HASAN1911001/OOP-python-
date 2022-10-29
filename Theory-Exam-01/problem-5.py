'''---------------------------------------------------------------------------------
5. Write a python program to read student_name and mark from keyboard and store the data 
in a text file with an unique studen_id .
-------------------------------------------------------------------------------------'''

# import random
# choices = list(range(100))
# random.shuffle(choices)
# print(choices.pop())

N = input("Number of Students: ")
N = int(N)
i=1

with open("student_info.txt",'w',encoding = 'utf-8') as f:
    f.write("student_id   student_name              marks")
    f.write("\n")

    while(i<=N):
        f.write(str(i))
        f.write("             ")
        f.write(input("Student Name: "))
        f.write("                    ")
        f.write(input("Marks: "))
        f.write("\n")
        i = i+1
    