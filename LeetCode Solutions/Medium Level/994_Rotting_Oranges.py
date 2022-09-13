'''
994. Rotting Oranges

Medium

8276

304

Add to List

Share
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
'''

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = set()
        fresh = []
        mins = 0
        visit = set()
        rotted = [False]
        
        def rot(r, c):
            if rotted[0] == True:
                return
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0 or (r, c) in visit:
                return
            if grid[r][c] == 2:
                rotted[0] = True
                return
            
            visit.add((r, c))
            if (rot(r+1, c) or rot(r-1, c) or rot(r, c+1) or rot(r, c-1)):
                return
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh.append([r, c])
                if grid[r][c] == 2:
                    rotten.add((r, c))
        
        if not fresh:
            return 0
        
        for r, c in fresh:
            rotted[0] = False
            rot(r, c)
            visit = set()
            if rotted[0] == False:
                return -1
        
        while fresh:
            mins += 1
            new = []
            for r, c in rotten:
                if [r+1, c] in fresh:
                    new.append([r+1, c])
                    fresh.remove([r+1, c])
                if [r-1, c] in fresh:
                    new.append([r-1, c])
                    fresh.remove([r-1, c])
                if [r, c+1] in fresh:
                    new.append([r, c+1])
                    fresh.remove([r, c+1])
                if [r, c-1] in fresh:
                    new.append([r, c-1])
                    fresh.remove([r, c-1])
            for r, c in new:
                rotten.add((r, c))
        
        return mins

'''
Success
Details 
Runtime: 72 ms, faster than 68.96% of Python3 online submissions for Rotting Oranges.
Memory Usage: 14 MB, less than 11.45% of Python3 online submissions for Rotting Oranges.
'''