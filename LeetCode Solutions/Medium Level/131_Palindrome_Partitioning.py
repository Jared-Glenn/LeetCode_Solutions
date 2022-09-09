'''
131. Palindrome Partitioning

Medium

8190

248

Add to List

Share
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.
'''
# Original Solution (Not working)

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        
        def backtracking(string, parts):
            print(string, parts)
            if len(string) == 1:
                parts.append(string)
                res.append(parts.copy())
                print(parts, res)
                parts.pop()
                return
            if len(string) < 1:
                res.append(parts)
                return
            
            temp = []
            i = 1
            while i <= len(string):
                newString = string[:i]
                x = 0
                y = -1
                check = True
                for j in range(len(newString)):
                    if string[x] == string[y]:
                        x += 1
                        y -= 1
                        continue
                    else:
                        check = False
                        break
                if check:
                    temp.append(newString)
                i += 1
            
            for t in temp:
                parts.append(t)
                newest = string[len(t):]
                print('newest', newest, 'parts', parts)
                backtracking(newest, parts)
                parts.pop()
        
        backtracking(s, [])
        print(res)
        return res

# Neatcode Solution

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        
        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
            
        
        dfs(0)
        return res
    
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True

'''
Success
Details 
Runtime: 1717 ms, faster than 5.00% of Python3 online submissions for Palindrome Partitioning.
Memory Usage: 30.4 MB, less than 24.76% of Python3 online submissions for Palindrome Partitioning.
'''