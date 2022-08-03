'''
11. Container With Most Water

Medium

18875

1028

Add to List

Share
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            length = right - left
            tall = min(height[left], height[right])
            area = length*tall
            if area > res:
                res = area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        
        
        #for i, left in enumerate(height):
        #    length = 1
        #    for j, right in enumerate(height[i+1:]):
        #        if left > right:
        #            tall = right
        #        else:
        #            tall = left
        #        area = length*tall
        #        if area > res:
        #            res = area
        #        length +=1
                    
        return res


'''
Success
Details 
Runtime: 705 ms, faster than 98.40% of Python3 online submissions for Container With Most Water.
Memory Usage: 27.6 MB, less than 15.08% of Python3 online submissions for Container With Most Water.
'''