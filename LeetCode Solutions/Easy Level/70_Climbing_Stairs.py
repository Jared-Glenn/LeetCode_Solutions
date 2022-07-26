'''
70. Climbing Stairs

Easy

13197

392

Add to List

Share
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        back = 0
        forward = 1
        steps = n
        
        while steps > 0:
            placeholder2 = forward
            forward = back + forward
            back = placeholder2
            steps -= 1
        
        return forward

'''
Success
Details 
Runtime: 36 ms, faster than 80.15% of Python3 online submissions for Climbing Stairs.
Memory Usage: 13.8 MB, less than 96.04% of Python3 online submissions for Climbing Stairs.
'''