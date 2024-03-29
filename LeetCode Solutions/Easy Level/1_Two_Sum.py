'''
1. Two Sum

Easy

35372

1119

Add to List

Share
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
'''
# Solution 1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for x, num_a in enumerate(nums):
            for y, num_b in enumerate(nums[x+1:]):
                if num_a + num_b == target:
                    lst = [x, (y+x+1)]
                    return lst


'''
Success
Details 
Runtime: 3328 ms, faster than 26.78% of Python3 online submissions for Two Sum.
Memory Usage: 14.8 MB, less than 95.48% of Python3 online submissions for Two Sum.
'''

# Solution 2
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hmap = {}
        
        for x, num in enumerate(nums):
            solution = target - num
            if solution in hmap:
                return [x, hmap[solution]]
            else:
                hmap[num] = x

'''
Success
Details 
Runtime: 73 ms, faster than 85.72% of Python3 online submissions for Two Sum.
Memory Usage: 15.2 MB, less than 24.31% of Python3 online submissions for Two Sum.
'''


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        map = {}

        for i, num in enumerate(nums):
            dif = target - num
            if dif in map:
                return [i, map[dif]]
            else:
                map[num] = i
                
# Accepted