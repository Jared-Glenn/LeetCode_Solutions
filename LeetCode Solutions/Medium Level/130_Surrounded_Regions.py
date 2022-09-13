'''
130. Surrounded Regions

Medium

5730

1342

Add to List

Share
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

 

Example 1:


Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.
Example 2:

Input: board = [["X"]]
Output: [["X"]]
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
'''

# First solution. Has difficulty catching the extreme portions of captured regions.

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visit = set()
        
        def capture(r, c, prev):
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                if prev == 'O':
                    return False
                else:
                    return True
            
            if board[r][c] == 'X' or (r, c) in visit:
                return True
            
            visit.add((r, c))
            if (capture(r+1, c, board[r][c]) and 
                capture(r-1, c, board[r][c]) and 
                capture(r, c+1, board[r][c]) and 
                capture(r, c-1, board[r][c])):
                
                board[r][c] = 'X'
                return True
            else:
                return False
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                visit = set()
                capture(r, c, None)

# Second Attempt. Tries to reverse the thinking. Capturing all but marked squares.

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visit = set()
        mark = set()
        ROWS = len(board)
        COLS = len(board[0])
        
        def capture(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] == 'X' or (r, c) in visit:
                return
            
            visit.add((r, c))
            mark.add((r, c))
            capture(r+1, c)
            capture(r-1, c)
            capture(r, c+1)
            capture(r, c-1)
        
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O' and (r in [0, ROWS-1] or c in [0, COLS-1]):
                    mark.add((r, c))
                    capture(r, c)
        
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in mark:
                    visit = set()
                    board[r][c] = 'X'

'''
Success
Details 
Runtime: 320 ms, faster than 20.95% of Python3 online submissions for Surrounded Regions.
Memory Usage: 16.2 MB, less than 32.67% of Python3 online submissions for Surrounded Regions.
'''