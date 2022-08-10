'''
704. Binary Search

Easy

5691

131

Add to List

Share
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        high = (len(nums)) - 1
        low = 0
        
        
        while True:
            mid = int((high+low)/2)
            print(mid)
            if nums[mid] == target:
                return mid
            elif low > high:
                return -1
            elif nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                return -1

'''
Success
Details 
Runtime: 246 ms, faster than 96.62% of Python3 online submissions for Binary Search.
Memory Usage: 15.5 MB, less than 72.10% of Python3 online submissions for Binary Search.
'''

# Solution 2

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = int((left + right)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1

'''
Success
Details 
Runtime: 334 ms, faster than 63.18% of Python3 online submissions for Binary Search.
Memory Usage: 15.5 MB, less than 72.77% of Python3 online submissions for Binary Search.
'''