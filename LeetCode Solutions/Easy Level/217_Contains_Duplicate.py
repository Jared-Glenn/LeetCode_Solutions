'''
217. Contains Duplicate

Easy

5792

993

Add to List

Share
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = {}
        res = False
        
        for num in nums:
            if num in counter:
                res = True
            else:
                counter[num] = 1
        
        return res

'''
Success
Details 
Runtime: 544 ms, faster than 73.56% of Python3 online submissions for Contains Duplicate.
Memory Usage: 25.9 MB, less than 93.27% of Python3 online submissions for Contains Duplicate.
'''