'''
17. Letter Combinations of a Phone Number

Medium

12436

753

Add to List

Share
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
'''

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'], 
                7: ['p', 'q', 'r', 's'], 8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}
        
        if not digits:
            return []
        
        res = []
        cur = []
        def backtracking(i):
            if i >= len(digits):
                new = ''.join(cur)
                if new not in res:
                    res.append(new)
                return
            
            for letter in phone[int(digits[i])]:
                cur.append(letter)
                backtracking(i+1)
                cur.pop()
        
        backtracking(0)
        return res

'''
Success
Details 
Runtime: 43 ms, faster than 66.31% of Python3 online submissions for Letter Combinations of a Phone Number.
Memory Usage: 14 MB, less than 31.69% of Python3 online submissions for Letter Combinations of a Phone Number.
'''