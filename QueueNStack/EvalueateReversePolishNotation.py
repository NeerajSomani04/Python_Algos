

# Solution 1 -
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        operators = ['+', '-', '*', '/']
        for _ in tokens:
            if _ not in operators:
                s.append(_)
            else:
                a = s.pop()
                b = s.pop()
                
                if _ == '/': 
                    v = int(float(b)/float(a))
                else:
                    v = eval(b+ _ +a)
                s.append(str(v))
        return int(s.pop())
        
''' Big-O efficiency 
time complexity - O(n) - because of for loop
space complexity - O(1) 
'''

