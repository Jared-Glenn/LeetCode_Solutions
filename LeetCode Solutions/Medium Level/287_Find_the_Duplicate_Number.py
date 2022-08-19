'''
287. Find the Duplicate Number

Medium

15826

2031

Add to List

Share
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
 

Constraints:

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.
 

Follow up:

How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?
'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[nums[0]]
        fast = nums[nums[nums[0]]]
        
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        second = nums[0]
        
        while slow != second:
            slow = nums[slow]
            second = nums[second]
            
        return slow

'''
Success
Details 
Runtime: 1321 ms, faster than 14.77% of Python3 online submissions for Find the Duplicate Number.
Memory Usage: 28 MB, less than 31.21% of Python3 online submissions for Find the Duplicate Number.
'''