'''
128. Longest Consecutive Sequence

Medium

12278

516

Add to List

Share
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
'''
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
        
#         count = {}
#         high = None
#         low = None
#         best = 1
        
#         for num in nums:
#             if high == None or high < num:
#                 high = num
#             if low == None or low > num:
#                 low = num
#             count[num] = 1 + count.get(num, 0)
        
#         for i in range((high+1)):
#             print("i:", i)
#             print("low:", low)
#             print("i plus low:", i+low)
#             if (i+low) in count:
#                 condition = 1
#                 while (i+low) + condition in count:
#                     print('condition check:', i+low+condition)
#                     condition += 1
#                 if condition > best:
#                     print("condition:", condition)
#                     best = condition
#                     print("best:",best)
        
#         return best


import statistics

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        count = {}
        condition = 1
        best = 1
        
        if len(nums) == 0:
            return 0
        
        nums = [*set(nums)]
        nums.sort()
        
        for x, num in enumerate(nums):
            try:
                if (num + 1) == nums[x+1]:
                    condition += 1
                    if condition > best:
                        best = condition
                else:
                    condition = 1
            except:
                pass
        
        return best


'''
Success
Details 
Runtime: 314 ms, faster than 99.04% of Python3 online submissions for Longest Consecutive Sequence.
Memory Usage: 29 MB, less than 31.01% of Python3 online submissions for Longest Consecutive Sequence.
'''