'''
238. Product of Array Except Self

Medium

13675

786

Add to List

Share
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        total = 1
        zero_total = 0
        one_zero = False
        multi_zero = False
        
        for num in nums:
            if num == 0:
                if one_zero == True:
                    multi_zero = True
                else:
                    one_zero = True
            else:
                total *= num
        
        print(total)
        
        for x, num in enumerate(nums):
            if multi_zero == True:
                nums[x] = 0
            elif one_zero == True:
                if num == 0:
                    nums[x] = total
                else:
                    nums[x] = 0
            else:
                nums[x] = int(total/num)
        
        return nums

'''
Success
Details 
Runtime: 313 ms, faster than 67.06% of Python3 online submissions for Product of Array Except Self.
Memory Usage: 21 MB, less than 84.63% of Python3 online submissions for Product of Array Except Self.
'''