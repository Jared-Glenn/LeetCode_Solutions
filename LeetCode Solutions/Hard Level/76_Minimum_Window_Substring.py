'''
76. Minimum Window Substring

Hard

11566

553

Add to List

Share
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?

'''

# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         t_letters = {}
#         s_letters = {}
#         res = ''
        
#         left = 0
#         right = len(t) - 1
        
#         for letter in t:
#             t_letters[letter] = 1 + t_letters.get(letter, 0)
        
#         for x in range(right):
#             if s[x] in t_letters:
#                 s_letters[s[x]] = 1 + s_letters.get(s[x], 0)
#                 if t_letters == s_letters:
#                     return s[left: (right+1)]
                
#         for x, letter in enumerate(s[:-(right)]):
#             print(letter)
#             if letter in s_letters and s_letters[letter] <= t_letters[letter]:
#                 right += 1
#             elif letter not in s_letters:
#                 left += 1
#             else:
#                 s_letters[letter] -= 1
#                 if s_letters[letter] == 0:
#                     del s_letters[letter]
#             if s[x] in t_letters:
#                 print(t_letters, s_letters)
#                 s_letters[s[x]] = 1 + s_letters.get(s[x], 0)
#                 if t_letters == s_letters and len(res) == 0:
#                     res = s[left: (right+1)]
#                 if t_letters == s_letters and len(res) > len(s[left: (right+1)]):
#                         res = s[left: (right+1)]
            
                
#         print(t_letters, s_letters)
#         print(s[left: (right+1)])
        
#         return res

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        countT, window = {}, {}
        
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float('infinity')
        l = 0
        
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            
            if c in countT and window[c] == countT[c]:
                have += 1
                
            while have == need:
                if (r + 1 - l) < resLen:
                    res = [l, r]
                    resLen = (r + 1 - l)
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
            
        l, r = res
        if resLen != float('infinity'):
            return s[l:(r+1)]
        else:
            return ""

'''
Success
Details 
Runtime: 167 ms, faster than 53.24% of Python3 online submissions for Minimum Window Substring.
Memory Usage: 14.7 MB, less than 36.34% of Python3 online submissions for Minimum Window Substring.
'''