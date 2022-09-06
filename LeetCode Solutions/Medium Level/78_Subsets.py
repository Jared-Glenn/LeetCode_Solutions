'''
78. Subsets

Medium

11871

170

Add to List

Share
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        subsets = []
        def dfs(i):
            if i >= len(nums):
                res.append(subsets.copy())
                return
            
            subsets.append(nums[i])
            dfs(i + 1)
            
            subsets.pop()
            dfs(i + 1)
            
        dfs(0)
        return res

'''
Success
Details 
Runtime: 30 ms, faster than 98.38% of Python3 online submissions for Subsets.
Memory Usage: 14.1 MB, less than 35.94% of Python3 online submissions for Subsets.
'''