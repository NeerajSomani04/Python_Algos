# 202 - https://leetcode.com/problems/happy-number/

# Solution 1: below solution is not correct, as it take O(n) space and it also doesn't pass for number "19" not sure why??

class Solution:
    def find_square_sum(self, t: str) -> int:
        return sum([int(y)*int(y) for y in t])
        
    def isHappy(self, n: int) -> bool:
        str_n = str(n)
        #print('n= ',n , 'and lenth of str_n: ',len(str_n))
        if n == 1:
            print('i am in true condition')
            #print('n= ',n , 'and lenth of str_n: ',len(str_n))
            return True
        elif len(str_n) == 1 and n!=1:
            #print('i am in false condition')
            #print('n= ',n , 'and lenth of str_n: ',len(str_n))
            return False
        else:
            returned_sum = self.find_square_sum(str_n)
            #print(returned_sum)
            self.isHappy(returned_sum)
        

# Solution 2: below solution is not working for number "2"
class Solution:
    def find_square_sum(self, t) -> int:
        _sum = 0
        while (t>0):
            digit = t % 10
            _sum = digit * digit
            t = t // 10
        return _sum
        
    def isHappy(self, n: int) -> bool:
        slow, fast = n, n
        while True:
            slow = self.find_square_sum(slow)
            fast = self.find_square_sum(self.find_square_sum(fast))
            if slow == fast:
                break
        return slow == 1
      
      
      
'''
Time Complexity #
The time complexity of the algorithm is difficult to determine. 
However we know the fact that all unhappy numbers eventually get stuck in the cycle: 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4
This sequence behavior tells us two things:
1. If the number NN is less than or equal to 1000, then we reach the cycle or ‘1’ in at most 1001 steps.
2. For N > 1000, suppose the number has ‘M’ digits and the next number is ‘N1’. 
From the above Wikipedia link, we know that the sum of the squares of the digits of ‘N’ is at most 9^2 M, or 81M 
(this will happen when all digits of ‘N’ are ‘9’).
This means:
1. N1 < 81M
2. As we know M = log(N+1)M=log(N+1)
3. Therefore: N1 < 81 * log(N+1)N1<81∗log(N+1) => N1 = O(logN)N1=O(logN)
This concludes that the above algorithm will have a time complexity of O(logN)O(logN).
Space Complexity 
The algorithm runs in constant space O(1)O(1).
'''
