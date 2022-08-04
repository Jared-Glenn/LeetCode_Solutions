'''
42. Trapping Rain Water

Hard

20726

290

Add to List

Share
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105

'''
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         res = 0
#         left = None
#         right = len(height) - 1
#         end = None
#         pos_wat = 0
        
#         while end == None:
#             if height[right] <= height[right-1]:
#                 right -= 1
#             else:
#                 end = right
#                 right = 0
        
#         while left == None:
#                 if height[right] <= height[right+1]:
#                     right += 1
#                 else:
#                     left = right
#                     right = right+1
        
#         print('start right:',right, 'left:', left)
#         while left < end:
#             if height[left] > height[right]:
#                 right += 1
#                 print('right:',right)
#             elif height[left] == height[right]:
#                 right += 1
#                 print('right:',right, 'left:', left)
#             else:
#                 highest = min(height[left], height[right])
#                 while left != right:
#                     pos_wat += highest - height[left]
#                     print('left:',left, 'pos:', pos_wat)
#                     left += 1
#                 res += pos_wat
#                 pos_wat = 0
                
#         max_height = max(height[left+1:end])
#         right = height.index(max_height, left+1, end)
#         print('new_right:', right)
        
#         if left == end:
#             return res
        
#         while left < end:
#             while left != right:
#                 if height[right] - height[left] > 0:
#                     pos_wat += height[right] - height[left]
#                     print('left:',left, 'pos:', pos_wat)
#                 left += 1
#             res += pos_wat
#             pos_wat = 0
#             try:
#                 max_height = max(height[left+1:end])
#                 right = height.index(max_height, left+1, end)
#                 print('new_right:', right)
#             except:
#                 if height[end] - height[left] > 0:
#                     res += height[end] - height[left]
#                 return res
        
#         return res

class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        
        left = 0
        right = len(height) - 1
        max_left = height[left]
        max_right = height[right]
        
        while left < right:
            if max_right < max_left:
                right -= 1
                if max_right - height[right] > 0:
                    res += max_right - height[right]
                if max_right < height[right]:
                    max_right = height[right]
            else:
                left += 1
                if max_left - height[left] > 0:
                    res += max_left - height[left]
                if max_left < height[left]:
                    max_left = height[left]
        
        return res



'''
Success
Details 
Runtime: 182 ms, faster than 62.98% of Python3 online submissions for Trapping Rain Water.
Memory Usage: 16 MB, less than 81.80% of Python3 online submissions for Trapping Rain Water.
'''