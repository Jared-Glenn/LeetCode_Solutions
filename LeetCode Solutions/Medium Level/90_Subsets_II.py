'''
90. Subsets II

Medium

6503

183

Add to List

Share
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
'''

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        subset = []
        def backtracking(i):
            temp = subset.copy()
            temp.sort()
            if temp not in res:
                res.append(temp.copy())
            if i >= len(nums):
                return
            
            subset.append(nums[i])
            backtracking(i+1)
            
            subset.pop()
            backtracking(i+1)
        
        backtracking(0)
        return res

'''
Success
Details 
Runtime: 127 ms, faster than 5.15% of Python3 online submissions for Subsets II.
Memory Usage: 14.1 MB, less than 93.84% of Python3 online submissions for Subsets II.
'''