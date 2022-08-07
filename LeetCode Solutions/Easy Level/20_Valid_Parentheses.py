'''
20. Valid Parentheses

Easy

14710

713

Add to List

Share
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for brac in s:
            if brac in ['(', '[', '{']:
                stack.append(brac)
            else:
                if len(stack) == 0:
                    return False
                elif stack[-1] == '(' and brac == ')':
                    stack.pop()
                    continue
                elif stack[-1] == '[' and brac == ']':
                    stack.pop()
                    continue
                elif stack[-1] == '{' and brac == '}':
                    stack.pop()
                    continue
                else:
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False
                

'''
Success
Details 
Runtime: 38 ms, faster than 80.37% of Python3 online submissions for Valid Parentheses.
Memory Usage: 13.9 MB, less than 25.50% of Python3 online submissions for Valid Parentheses.

'''