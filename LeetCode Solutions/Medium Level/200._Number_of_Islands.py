'''
200. Number of Islands

Medium

15050

353

Add to List

Share
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def fill_island(x, y):
            print(x, y)
            if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid) or int(grid[y][x]) != 1:
                print('failed')
                return
            grid[y][x] = 2
            print(grid[y][x])
                
            fill_island(x+1,y)
            fill_island(x-1,y)
            fill_island(x,y+1)
            fill_island(x,y-1)
        
        count = 0
        
        for y, lst in enumerate(grid):
            for x, num in enumerate(lst):
                num = int(num)
                if num == 1:
                    fill_island(x,y)
                    count += 1
        
        print(grid)
        return count
    
'''
Success
Details 
Runtime: 872 ms, faster than 5.03% of Python3 online submissions for Number of Islands.
Memory Usage: 17 MB, less than 38.38% of Python3 online submissions for Number of Islands.
'''


# Alternate solution (Not better)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0
        
        def bfs(r,c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))
            while q:
                row, col = q.pop()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and
                       c in range(cols) and
                       grid[r][c] == '1' and
                       (r,c) not in visit):
                        q.append((r,c)) 
                        visit.add((r,c))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visit:
                    bfs(r,c)
                    islands += 1
        
        return islands


'''
Success
Details 
Runtime: 849 ms, faster than 5.03% of Python3 online submissions for Number of Islands.
Memory Usage: 21.9 MB, less than 19.34% of Python3 online submissions for Number of Islands.
'''