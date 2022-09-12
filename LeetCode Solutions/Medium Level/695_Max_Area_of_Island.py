'''
695. Max Area of Island

Medium

7861

176

Add to List

Share
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

 

Example 1:


Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
'''

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        biggestArea = [0]
        visited = set()
        area = [0]
        
        def areaFinder(r, c):
            if (r, c) in visited or r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0:
                return
            
            visited.add((r, c))
            area[0] += 1
            if area[0] > biggestArea[0]:
                biggestArea[0] = area[0]
            
            areaFinder(r+1, c)
            areaFinder(r-1, c)
            areaFinder(r, c+1)
            areaFinder(r, c-1)
        
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area[0] = 0
                    areaFinder(r, c)
        
        return biggestArea[0]

'''
Success
Details 
Runtime: 322 ms, faster than 11.37% of Python3 online submissions for Max Area of Island.
Memory Usage: 17.6 MB, less than 36.23% of Python3 online submissions for Max Area of Island.
'''