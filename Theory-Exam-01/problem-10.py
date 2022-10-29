'''---------------------------------------------------------------------------------
10. Write a Python class named Distance constructed by two points (x1, y1), (x2, y2) and 
a method which will compute the distance between those points.
-------------------------------------------------------------------------------------'''
import math

class Distance:
    def  __init__(self, A, B):
        self.A = A
        self.B = B
    
    def distance(self):
        distance = math.sqrt( ((self.A[0]-self.B[0])**2)+((self.A[1]-self.B[1])**2) )
        print(distance)



p1 = [4, 0]
p2 = [6, 6]

obj = Distance(p1, p2)

obj.distance()
