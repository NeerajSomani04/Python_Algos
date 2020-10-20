# Lets follow our procedure to solve this question:
'''
Definition - can be understood from question (https://leetcode.com/explore/learn/card/queue-stack/231/practical-application-queue/1374/)

Data - 
  - Input - an m x n 2d grid map of '1's (land) and '0's (water)
  - output - return the number of islands.
  - Edge case - 
  - assumptions - grid can't be empty
  Constraints:
      m == grid.length
      n == grid[i].length
      1 <= m, n <= 300
      grid[i][j] is '0' or '1'.
  
Pseudo code - 
  - 
  - 
'''

# Actual Code 
# Solution 1 -
class Solution:
    def is_valid(self, grid, r, c):
        m, n = len(grid), len(grid[0])
        if r < 0 or c < 0 or r >= m or c >= n:
            return False
        return True
    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.bfs(grid, i, j)
                    count += 1
        return count

    def bfs(self, grid, r, c):
        queue = collections.deque()
        queue.append((r, c))
        print('queue after append', queue)
        grid[r][c] = '2'
        print("grid after updating '1' to '2'", grid)
        while queue:
            directions = [(0,1), (0,-1), (-1,0), (1,0)]
            r, c = queue.popleft()
            print("queue after popping left element", queue)
            for d in directions:
                nr, nc = r + d[0], c + d[1]    
                if self.is_valid(grid, nr, nc) and grid[nr][nc] == '1':
                    queue.append((nr, nc))
                    print("queue after appending new nr, nc", queue)
                    grid[nr][nc] = '2'
                    print("grid after updating new '1' to '2'", grid)

''' Big-O efficiency 
# time complexity - O(n*m) - because of 2 for loop
# space complexity - 
'''
