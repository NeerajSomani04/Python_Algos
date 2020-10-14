# Lets follow our procedure to solve this question:
'''
Definition - can be understood from question (https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1148/)
Data - 
  - Input - a array that contains some intergers
  - output - return third maximum number in array
  - Edge case - number can vary from any negative to position number, array length can be one to infinity.
  - assumptions - array can't be empty
  
Pseudo code - 
  - create an empty array that contains only 3 maximum element at any iteration of nums array
  - run through each element of array and check if new element is greater than min(array) 
    - replace it
    - return third max of array after sorting it
'''

# Actual Code 
# solution 1 -
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = ''.join(map(str, digits))
        digits = str(int(digits)+1)
        digits = list(map(int,digits))
        print(digits)
        return digits

''' Big-O efficiency
# time complexity - O(n*n)
# space complexity - O(1)

# Above solution is quadratic solution in terms of time complexity, if we increase the size of n to a great amount. Its not a good solution.

from timeit import timeit
for e in range(15, 23):
    digits = 2**e * [1]
    print(timeit(lambda: [int(i) for i in str(int(''.join(map(str,digits)))+1)], number=1))

0.10307004694835681
0.3856829295774648
1.4858273051643196
5.850462647887324
23.374171342723006
94.15480187793428
383.15695864788734
1525.5406662910798
'''

# Solution 2 - Need to understand this solution
class Solution:
    def plusOne(self, digits):
        for i in range(len(digits)):
            if digits[~i] < 9:
                digits[~i] += 1
                return digits
            digits[~i] = 0
        return [1] + [0] * len(digits)


# Solution 3 - Need to understand this solution
def plusOne(self, digits):
    length = len(digits) - 1
    while digits[length] == 9:
        digits[length] = 0
        length -= 1
    if(length < 0):
        digits = [1] + digits
    else:
        digits[length] += 1
    return digits
