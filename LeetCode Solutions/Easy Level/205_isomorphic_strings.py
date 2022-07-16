'''
205. Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true

'''
# First old solution. Second got closer, but had to study outside sources to find the final solution.

# class Solution(object):
#     def isIsomorphic(self, s, t):
#         s_list = list(s)
#         t_list = list(t)
        
#         for x, s_letter in enumerate(s_list):
#             for y, t_letter in enumerate(t_list):
#                 if x == y:
#                     s_list[x] = t_letter
#                 else:
#                     pass
                
#         if s_list == t_list:
#             return True
#         else:
#             return False

class Solution(object):
    def isIsomorphic(self, s, t):
        
        s_dictionary = {}
        t_dictionary = {}
        
        for s_letter, t_letter in zip(s, t):
            if (s_letter not in s_dictionary) and (t_letter not in t_dictionary):
                s_dictionary[s_letter] = t_letter
                t_dictionary[t_letter] = s_letter
            elif (s_dictionary.get(s_letter) != t_letter) or (t_dictionary.get(t_letter) != s_letter):
                return False
        return True
        


'''
Success
Details 
Runtime: 49 ms, faster than 54.84% of Python online submissions for Isomorphic Strings.
Memory Usage: 16.4 MB, less than 7.47% of Python online submissions for Isomorphic Strings.

'''