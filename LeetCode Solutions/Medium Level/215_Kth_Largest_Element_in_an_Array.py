'''
215. Kth Largest Element in an Array

Medium

11647

587

Add to List

Share
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

You must solve it in O(n) time complexity.

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
'''

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-s for s in nums]
        
        heapq.heapify(nums)
        
        for i in range(k):
            res = heapq.heappop(nums)
        
        return -1*(res)

'''
Success
Details 
Runtime: 978 ms, faster than 32.96% of Python3 online submissions for Kth Largest Element in an Array.
Memory Usage: 27.3 MB, less than 33.95% of Python3 online submissions for Kth Largest Element in an Array.
'''