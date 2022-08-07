'''
239. Sliding Window Maximum

Hard

11338

373

Add to List

Share
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
'''

# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         if k > len(nums): return
        
#         res, window = [], {}
#         l = 0
#         biggest = float('-inf')
        
#         for r, num in enumerate(nums):
#             window[num] = 1 + window.get(num, 0)
#             if num > biggest:
#                 biggest = num
#             if (r+1) >= k:
#                 res.append(biggest)
#                 window[nums[l]] -= 1
#                 if window[nums[l]] == 0:
#                     del window[nums[l]]
#                 if nums[l] == biggest and len(window) != 0:
#                     biggest = max(window)
#                 elif len(window) == 0:
#                     try:
#                         biggest = nums[l+1]
#                     except:
#                         pass
#                 l += 1
                
            
#         return res


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque()
        l = r = 0
        
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            
            if l > q[0]:
                q.popleft()
            
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r +=1
        
        return output


'''
Success
Details 
Runtime: 2526 ms, faster than 65.91% of Python3 online submissions for Sliding Window Maximum.
Memory Usage: 30 MB, less than 45.91% of Python3 online submissions for Sliding Window Maximum.

'''