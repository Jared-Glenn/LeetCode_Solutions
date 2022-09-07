'''
46. Permutations

Medium

12755

217

Add to List

Share
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        if (len(nums) == 1):
            return [nums[:]]
        
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            
            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)
        
        return result

'''
Success
Details 
Runtime: 70 ms, faster than 36.10% of Python3 online submissions for Permutations.
Memory Usage: 14.1 MB, less than 58.77% of Python3 online submissions for Permutations.


REVIEW REQUIRED - REVIEW REQUIRED - REVIEW REQUIRED - REVIEW REQUIRED - REVIEW REQUIRED
'''

# Easier to understand solution, but it is somewhat slower.

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        res = []
        self.backtracking(res, visited, [], nums)
        return res
    
    def backtracking(self, res, visited, subset, nums):
        if len(subset) == len(nums):
            res.append(subset)
        for i in range(len(nums)):
            if i not in visited:
                visited.add(i)
                self.backtracking(res, visited, subset+[nums[i]], nums)
                visited.remove(i)

'''
Success
Details 
Runtime: 95 ms, faster than 5.05% of Python3 online submissions for Permutations.
Memory Usage: 14 MB, less than 58.77% of Python3 online submissions for Permutations.
'''