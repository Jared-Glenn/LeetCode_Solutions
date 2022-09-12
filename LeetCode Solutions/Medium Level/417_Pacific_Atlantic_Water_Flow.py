'''
417. Pacific Atlantic Water Flow

Medium

5556

1048

Add to List

Share
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

 

Example 1:


Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
Example 2:

Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.
 

Constraints:

m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 105
'''

# Working model that runs a bit too slow for this problem (passed 112 out of 113)

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        end = []
        visited = set()
        
        def flow(r, c, prev):
            if r < 0 or c < 0:
                end.append('P')
                return
            if r >= len(heights) or c >= len(heights[0]):
                end.append('A')
                return
            if heights[r][c] > prev or (r, c) in visited:
                return
            
            visited.add((r, c))
            flow(r+1, c, heights[r][c])
            flow(r-1, c, heights[r][c])
            flow(r, c+1, heights[r][c])
            flow(r, c-1, heights[r][c])
        
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                flow(r, c, float('inf'))
                if 'A' in end and 'P' in end:
                    res.append([r, c])
                end = []
                visited = set()
        
        return res



# Second Solution (Optimization idea by Neatcode. Code by me.)

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        visitPacific = set()
        visitAtlantic = set()
        res = []
        
        def pacFlow(r, c, prev):
            if r >= len(heights) or r < 0 or c >= len(heights[0]) or c < 0 or heights[r][c] < prev or (r, c) in visitPacific:
                return
            
            visitPacific.add((r, c))
            pacFlow(r+1, c, heights[r][c])
            pacFlow(r-1, c, heights[r][c])
            pacFlow(r, c+1, heights[r][c])
            pacFlow(r, c-1, heights[r][c])
        
        
        def atFlow(r, c, prev):
            if r >= len(heights) or r < 0 or c >= len(heights[0]) or c < 0 or heights[r][c] < prev or (r, c) in visitAtlantic:
                return
            
            visitAtlantic.add((r, c))
            atFlow(r+1, c, heights[r][c])
            atFlow(r-1, c, heights[r][c])
            atFlow(r, c+1, heights[r][c])
            atFlow(r, c-1, heights[r][c])
        
        
        for c in range(len(heights[0])):
            pacFlow(0, c, float('-inf'))
        
        for r in range(len(heights)):
            pacFlow(r, 0, float('-inf'))
        
        for c in range(len(heights[0])):
            atFlow(len(heights) - 1, c, float('-inf'))
        
        for r in range(len(heights)):
            atFlow(r, len(heights[0]) - 1, float('-inf'))
        
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if (r, c) in visitPacific and (r, c) in visitAtlantic:
                    res.append([r, c])
        
        return res

'''
Success
Details 
Runtime: 617 ms, faster than 28.02% of Python3 online submissions for Pacific Atlantic Water Flow.
Memory Usage: 16.2 MB, less than 13.54% of Python3 online submissions for Pacific Atlantic Water Flow.
'''