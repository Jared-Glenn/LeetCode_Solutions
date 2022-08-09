'''
22. Generate Parentheses

Medium

14435

542

Add to List

Share
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        lst = []
        res = []
        
        def parentheses(left_num, right_num):
            if left_num == right_num == n:
                version = "".join(lst)
                res.append(version)
                return
            
            if left_num > right_num:
                lst.append(')')
                parentheses(left_num, right_num + 1)
                lst.pop()
                
            if left_num < n:
                lst.append('(')
                parentheses(left_num+1, right_num)
                lst.pop()
            
        parentheses(0,0)
            
        return res

'''
Success
Details 
Runtime: 40 ms, faster than 86.10% of Python3 online submissions for Generate Parentheses.
Memory Usage: 14.1 MB, less than 76.94% of Python3 online submissions for Generate Parentheses.

'''