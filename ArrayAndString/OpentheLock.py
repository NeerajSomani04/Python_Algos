# Lets follow our procedure to solve this question:
'''
Definition - can be understood from question (https://leetcode.com/explore/learn/card/queue-stack/231/practical-application-queue/1375/)
Data - 
  - Input - given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.
  - output - the minimum total number of turns required to open the lock, or -1 if it is impossible.
  - Edge case - 
  - assumptions - 
        Constraints:
            1 <= deadends.length <= 500
            deadends[i].length == 4
            target.length == 4
            target will not be in the list deadends.
            target and deadends[i] consist of digits only.
  
Pseudo code - 
  - initiate a variable start position of lock
  - if start in deadends, return -1
  - elif, start == target, return 0
  -- else,   
    - create an empty queue
    - add start to empty queue
    - create possile combinations from this start position
    - increment counter to keep track of moves
    - if any of these equals to target, return counter 
    - else, check each element agaist deadends array, append only those elements into queue which are not in deadends
    - continue this untill queue is empty or you meet the target
    - 
'''

'''
Why would DFS not work for this problem ?
# Yes, definitely you can apply DFS here. As the whole search space is 10^4 = 10000, DFS can work here too. But why many people choose BFS instead? Because the problem here asks for the minimum number of steps to achieve the target state. Using BFS, we can report the answer as long as we reach the target state. But using DFS, we can't guarantee that the initial target state that we reach is the optimal solution. You still have to search the whole search space. Think about the problem that to find the depth of a binary tree, it is quite similar in this sense.
# In dfs we have to search even after getting solution for this problem.
# If a BFS finds the target node, it is guaranteed to be the shortest path or the minimum total number of turns required to open the lock as stated in the problem. A DFS can find the minimum path, but it can only be sure its the minimum after checking every possible path.
'''

# Actual Code 
# Solution 1 - with deque -
class Solution:
    def openLock(self, deadends, target):
            marker, depth = 'x', -1
            visited, q = set(deadends), deque(['0000'])

            while q:
                size = len(q)
                depth += 1
                for _ in range(size):
                    node = q.popleft()
                    if node == target: return depth
                    if node in visited: continue
                    visited.add(node)
                    q.extend(self.successors(node))
            return -1

    def successors(self, src):
        res = []
        for i, ch in enumerate(src):
            num = int(ch)
            res.append(src[:i] + str((num - 1) % 10) + src[i+1:])
            res.append(src[:i] + str((num + 1) % 10) + src[i+1:])
        return res
        
''' Big-O efficiency -
time complexity - 
space complexity - 
'''

# Solution 2 - without deque (Below solution needs to be corrected)

class Solution:
    def openLock(self, deadends, target):
        deadends, level, ln, visited = set(deadends), ["0000"], 0, set('0000')
        
        if "0000" in deadends: return -1
        
        while level:
            new_level, ln = [], ln+1
            for item in level:
                for i in range(4):
                    for move in [-1, 1]:
                        new_digit = (int(item[i]) + move) % 10
                        new_item = item[:i] + str(new_digit) + item[i+1:]
                        
                        if new_item == target:
                            return ln
                        if new_item not in visited and new_item not in deadends:
                            visited.add(new_item)
                            new_level.append(new_item)
            level = new_level
        return -1



# Solution - 3
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:  
        # set is hashtable which makes accessing faster. 
        deadends = set(deadends)
        # Dealing with sepcial conditions
        
        if "0000" in deadends: return -1      
        if target == "0000": return 0
        
        # Initialize bfs queue and visited dictionary to avoid going back
        queue = collections.deque()
        visited = {}
        queue.append(["0000", 0])
        
        while len(queue) > 0:   
            current, level = queue.popleft()            
            new_nums = []       
            
            # Collect all connected numbers (8 of them)
            for i in range(4):
                new_nums.append(current[:i] + str((int(current[i]) + 1) % 10) + current[i+1:])                
                new_nums.append(current[:i] + str((int(current[i]) - 1) % 10) + current[i+1:])
            
            # Either append new number to queue with one level deeper or just pass it if visited or deadend
            for num in new_nums:
                if num in visited or num in deadends:
                    continue
                visited[num] = True                
                if num == target:
                    return level + 1
                queue.append([num, level + 1])                
        return -1    
        
        

