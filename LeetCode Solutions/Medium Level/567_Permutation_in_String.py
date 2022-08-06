'''
567. Permutation in String

Medium

6699

210

Add to List

Share
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        letters1 = {}
        letters2 = {}
        
        for letter in s1:
            letters1[letter] = 1 + letters1.get(letter, 0)
        
        if len(s2) < len(s1):
            return False
        
        if len(s1) == 1:
            if s1[0] in s2:
                return True
            else:
                return False
        
        left = 0
        right = len(s1) - 1
        length = len(s1) - 1
        
        for x, letter in enumerate(s2[:(length+1)]):
            letters2[letter] = 1 + letters2.get(letter, 0)
            if letters2 == letters1:
                return True
        
        print(letters1, letters2)
        
        for x in range(len(s2[:-(length)])):
            letters2[s2[left]] -= 1
            if letters2[s2[left]] == 0:
                del letters2[s2[left]]
            left += 1
            right += 1
            try:
                letters2[s2[right]] = 1 + letters2.get(s2[right], 0)
                if letters2 == letters1:
                    return True
            except:
                return False
        
        return False


'''
Success
Details 
Runtime: 68 ms, faster than 95.28% of Python3 online submissions for Permutation in String.
Memory Usage: 14 MB, less than 68.65% of Python3 online submissions for Permutation in String.
'''