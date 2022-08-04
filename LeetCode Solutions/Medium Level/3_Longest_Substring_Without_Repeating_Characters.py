'''
3. Longest Substring Without Repeating Characters

Medium

27141

1175

Add to List

Share
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        lst = []
        first = 0
        
        for x, letter in enumerate(s):
            if letter in lst:
                while letter in lst:
                    lst.remove(s[first])
                    first += 1
                lst.append(letter)
            else:
                lst.append(letter)
                if (x+1) - first > res:
                    res = (x+1) - first
        
        return res


'''
Success
Details 
Runtime: 109 ms, faster than 48.46% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 14 MB, less than 93.16% of Python3 online submissions for Longest Substring Without Repeating Characters.
'''