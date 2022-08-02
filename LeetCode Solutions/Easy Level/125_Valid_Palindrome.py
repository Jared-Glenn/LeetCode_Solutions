'''
125. Valid Palindrome

Easy

4343

5679

Add to List

Share
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        string = re.sub(r'[^a-z0-9]', '', s)
        forward = 0
        backward = -1
        
        for letter in string:
            if string[forward] == string[backward]:
                forward += 1
                backward -= 1
            else:
                return False
        
        return True

'''
Success
Details 
Runtime: 46 ms, faster than 94.95% of Python3 online submissions for Valid Palindrome.
Memory Usage: 15.5 MB, less than 20.08% of Python3 online submissions for Valid Palindrome.
'''