'''
392. Is Subsequence

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false

'''

class Solution(object):
    def isSubsequence(self, s, t):
        s_list = list(s)
        t_list = list(t)
        
        print(s_list)
        print(t_list)
        
        t_length = len(t_list) - 1
        
        for s_letter in s_list:
            if len(t_list) > 0:
                for x, t_letter in enumerate(t_list):
                    if s_letter == t_letter:
                        print(s_letter,"equaling",t_letter)
                        del t_list[:(x+1)]
                        t_length = len(t_list) - 1
                        break
                    elif s_letter != t_letter and x == t_length:
                        return False
                    else:
                        print(s_letter,"not equaling",t_letter)
                        pass
            else:
                return False
        
        
        return True
                
'''
Success
Details 
Runtime: 335 ms, faster than 5.02% of Python online submissions for Is Subsequence.
Memory Usage: 13.7 MB, less than 47.99% of Python online submissions for Is Subsequence.
'''