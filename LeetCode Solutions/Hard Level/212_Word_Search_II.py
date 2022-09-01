'''
212. Word Search II

Hard

6678

282

Add to List

Share
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example 1:


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:


Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.
'''
# First Written Solution - Tried to build the search function into the Trie class
# itself. This does not allow us to record solutions.

class TrieNode():
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.list = []
    
    def insert(self, word):
        cur = self.root
        
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        
        cur.end = True
        
    def search(self, root, letter, x, y, board):
        board[y][x] = 0
        
        # Is the letter in the current box among the possible next letters?
        if letter in root.children:
            # If so, move into that node and add the letter to our word list
            print(letter)
            root = root.children[letter]
            self.list.append(letter)
            print(self.list)
            # If it's the end of the word, stop searching.
            if root.end:
                return self.list
        
        # If the current letter is not in the list, revert the word list and stop searching this branch.
        else:
            return False
        
        if y + 1 < len(board):
            up = self.search(root, board[y+1][x], x, y+1, board)
        if y > 0:
            down = self.search(root, board[y-1][x], x, y-1, board)
        if x + 1 < len(board[y]):
            right = self.search(root, board[y][x+1], x+1, y, board)
        if x > 0:
            left = self.search(root, board[y][x-1], x-1, y, board)
        
        
        return
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        trie = Trie()
        res = []
        
        for word in words:
            trie.insert(word)
        
        for y, word in enumerate(words):
            for x, c in enumerate(word):
                print(y, x)
                newboard = board
                if trie.list:
                    res.append(''.join(trie.list))
                #trie.list = []
                trie.search(trie.root, c, x, y, newboard)
        
        print(res)
        
        return res

# Solution inspired by NeatCode (Added optimization by removing words from Trie
# after being found.)

class TrieNode():
    def __init__(self):
        self.children = {}
        self.end = False
    
    def insert(self, word):
        cur = self
        
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        
        cur.end = True
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        trie = TrieNode()
        
        for word in words:
            trie.insert(word)
    
        ROWS, COLUMNS = len(board), len(board[0])
        res, visit, new = set(), set(), set()
    
        def dfs(r, c, root, word):
            if (r < 0 or r == ROWS or c < 0 or c == COLUMNS or board[r][c] not in root.children or (board[r][c] in visit and visit)):
                return
            
            visit.add((r, c))
            root = root.children[board[r][c]]
            word += board[r][c]
            if root.end:
                res.add(word)
                new.add(word)
            dfs(r+1, c, root, word)
            dfs(r-1, c, root, word)
            dfs(r, c+1, root, word)
            dfs(r, c-1, root, word)
            
            print(r, c, visit, res)
            visit.remove((r, c))
        
        for r in range(ROWS):
            for c in range(COLUMNS):
                dfs(r, c, trie, '')
                if new:
                    for word in new:
                        words.remove(word)
                    new = set()
                    trie = TrieNode()
                    for word in words:
                        trie.insert(word)
        
        return list(res)

'''

'''