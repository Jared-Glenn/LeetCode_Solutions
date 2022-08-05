'''
424. Longest Repeating Character Replacement

Medium

5411

213

Add to List

Share
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length

'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hshmap = {}
        
        l = 0
        res = 0
        for r in range(len(s)):
            hshmap[s[r]] = 1 + hshmap.get(s[r], 0)
            length = (r + 1) - l
            if (length -(max(hshmap.values()))) <= k:
                if length > res:
                    res = length
            else:
                while (length -(max(hshmap.values()))) > k:
                    hshmap[s[l]] -= 1
                    l += 1
                    length = (r + 1) - l
        return res


'''
Success
Details 
Runtime: 224 ms, faster than 44.00% of Python3 online submissions for Longest Repeating Character Replacement.
Memory Usage: 14 MB, less than 57.73% of Python3 online submissions for Longest Repeating Character Replacement.
'''
'''
--ATTEMPT TWO--ATTEMPT TWO--ATTEMPT TWO--ATTEMPT TWO--ATTEMPT TWO--ATTEMPT TWO--ATTEMPT TWO--ATTEMPT TWO--ATTEMPT TWO--ATTEMPT TWO--ATTEMPT TWO--ATTEMPT TWO--ATTEMPT TWO--
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letters = {}
        first = 0
        res = 0

        for x, letter in enumerate(s):
            letters[letter] = 1 + letters.get(letter, 0)
            if max(letters.values()) + k >= (x+1) - first:
                if (x+1) - first > res:
                    res = (x+1) - first
            else:
                while max(letters.values()) + k < (x+1) - first:
                    position = s[first]
                    letters[position] -= 1
                    first += 1
                
        return res
    
'''
Success
Details 
Runtime: 362 ms, faster than 14.93% of Python3 online submissions for Longest Repeating Character Replacement.
Memory Usage: 14 MB, less than 58.30% of Python3 online submissions for Longest Repeating Character Replacement.
'''