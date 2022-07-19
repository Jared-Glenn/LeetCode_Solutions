'''
409. Longest Palindrome

Easy

3093

177

Add to List

Share
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
 
'''

class Solution:
    def longestPalindrome(self, s: str) -> int:
        orig_list = list(s)
        doubles = []
        single = None
        palindrome = []
        
        while len(orig_list) > 0:
            letter = orig_list.pop(0)
            if letter in orig_list:
                orig_list.remove(letter)
                doubles.append(letter)
            else:
                single = letter
        
        for letter in doubles:
            palindrome.insert(0, letter)
            palindrome.append(letter)
        
        if single != None:
            middle = int((len(palindrome))/2)
            palindrome.insert(middle, single)

        return len(palindrome)


'''
Success
Details 
Runtime: 72 ms, faster than 8.86% of Python3 online submissions for Longest Palindrome.
Memory Usage: 14 MB, less than 22.22% of Python3 online submissions for Longest Palindrome.
'''