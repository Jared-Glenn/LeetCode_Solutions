'''
51. N-Queens

Hard

8195

188

Add to List

Share
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

Example 1:


Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]
 

Constraints:

1 <= n <= 9
'''

# First attempt. Tried to just get positions of the columns for the queens,
# but this led to very confusing variables.

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cur  = []
        
        def backtracking(r, q):
            if q == n:
                res.append(cur.copy())
                return
            if r >= n:
                return
            
            for c in range(n):
                if not cur:
                    cur.append(c)
                    backtracking(r+1, q+1)
                    cur.pop()
                if c not in cur:
                    for col, row in enumerate(cur):
                        print('r', r, 'c', c, 'row', row, 'col', col)
                        if (r-c) == (row-col) or (r+c) == (row+col):
                            continue
                        else:
                            cur.append(c)
                            backtracking(r+1, q+1)
                            cur.pop()
            
            backtracking(r+1, q)
                    
                    
                    
                    
                    
                    
                #if not cur:
                #    cur.append(c)
                #    backtracking(r+1, q+1)
                #    cur.pop()
                #    
                #    for row in range(len(cur)):
                #        mod = r - row
                #        print('c', c, 'mod', mod, 'r', r, 'row', row, 'cur', cur)
                #        if c + mod == cur[r - mod] or abs(c - mod) == cur[r - mod]:
                #            print('nope!')
                #            continue
                #        else:
                #            print('yep!')
                #            cur.append(c)
                #            backtracking(r+1, q+1)
                #            cur.pop()
        
        backtracking(0, 0)
        print(res)


# Second solution. Makes use of three sets to keep track of where queens are. Neatcode solution.

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set() # (c+r)
        negDiag = set() # (c-r)
        
        res = []
        board = [["."] * n for i in range(n)]
        
        def backtracking(r):
            if r >= n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c not in col and (c+r) not in posDiag and (c-r) not in negDiag:
                    col.add(c)
                    posDiag.add(c+r)
                    negDiag.add(c-r)
                    board[r][c] = "Q"
                    
                    backtracking(r+1)
                    
                    col.remove(c)
                    posDiag.remove(c+r)
                    negDiag.remove(c-r)
                    board[r][c] = "."
        
        backtracking(0)
        return res

'''
Success
Details 
Runtime: 132 ms, faster than 37.91% of Python3 online submissions for N-Queens.
Memory Usage: 14.4 MB, less than 46.42% of Python3 online submissions for N-Queens.
'''