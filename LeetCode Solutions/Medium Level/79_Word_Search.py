'''
79. Word Search

Medium

10816

403

Add to List

Share
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
 

Follow up: Could you use search pruning to make your solution faster with a larger board?
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res = [False]
        wordLen = len(word)
        
        def gridSearch(x, y, cord, visit):
            if cord == wordLen:
                res[0] = True
                return
            if x >= len(board) or x < 0 or y >= len(board[0]) or y < 0 or cord >= wordLen or word[cord] != board[x][y] or [x,y] in visit:
                return
            
            visit.append([x,y])
            gridSearch(x-1, y, cord + 1, visit)
            gridSearch(x+1, y, cord + 1, visit)
            gridSearch(x, y-1, cord + 1, visit)
            gridSearch(x, y+1, cord + 1, visit)
            visit.remove([x,y])
            
        
        newWord = list(word)
        for i, row in enumerate(board):
            for j, column in enumerate(board[i]):
                if board[i][j] in newWord:
                    newWord.remove(board[i][j])
        
        if newWord:
            return False
        else:
            for i, row in enumerate(board):
                for j, column in enumerate(board[i]):
                    if res == True:
                        break
                    if board[i][j] == word[0]:
                        gridSearch(i, j, 0, [])
        
        return res[0]

'''
Success
Details 
Runtime: 4650 ms, faster than 90.29% of Python3 online submissions for Word Search.
Memory Usage: 14 MB, less than 50.62% of Python3 online submissions for Word Search.
'''