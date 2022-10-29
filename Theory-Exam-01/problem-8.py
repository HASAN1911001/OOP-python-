'''---------------------------------------------------------------------------------
8. Write a Python class to find a pair of elements (indices of the two numbers) from a
given array whose sum equals a specific target number.

Input:
numbers= [10,20,10,40,50,60,70]
target=50 
Output: 3, 4
-------------------------------------------------------------------------------------'''

class solution:
  def twoSum(self, numbers, target):
       lookup = {}
       for i, num in enumerate(numbers):
           if target - num in lookup:
               return (lookup[target - num]+1, i+1 )
           lookup[num] = i


print("Outptu: %d, %d" % solution().twoSum((10,20,10,40,50,60,70),50))