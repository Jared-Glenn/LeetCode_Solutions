"""
724. Find Pivot Index

Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

 

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
Example 3:

Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0
 

Constraints:

1 <= nums.length <= 104
-1000 <= nums[i] <= 1000



"""

import numpy as np

class Solution(object):
    def pivotIndex(self, nums):
        nums = np.array(nums)
        for x, num in enumerate(nums):
            to_the_left = x
            if to_the_left >= 0:
                left_sum = nums[:to_the_left].sum()
            else:
                left_sum = 0
            to_the_right = x + 1
            if to_the_right < len(nums):
                right_sum = nums[to_the_right:].sum()
            else:
                right_sum = 0
            if left_sum == right_sum:
                if to_the_left <= 0:
                    return 0
                else:
                    return x
            if x + 1 == len(nums):
                return -1
            
            
"""
Success
Details 
Runtime: 791 ms, faster than 27.25% of Python online submissions for Find Pivot Index.
Memory Usage: 26.7 MB, less than 6.04% of Python online submissions for Find Pivot Index.
Next challenges:
Subarray Sum Equals K
Find the Middle Index in Array
Number of Ways to Split Array
Maximum Sum Score of Array

"""