'''
746. Min Cost Climbing Stairs

Easy

7298

1184

Add to List

Share
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

 

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
 
'''
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        cost.append(0)
        
        for x in range(len(cost) - 3, -1, -1):
            cost[x] += min(cost[x+1], cost[x+2])
        
        return min(cost[0], cost[1])
        
        
        #cost.append(0)
        #i = -1
        #
        #for x in reversed(cost):
        #    if i > -3:
        #        i -= 1
        #        continue
        #    if cost[i+1] < cost[i+2]:
        #        cost[i] = x + cost[i+1]
        #    else:
        #        cost[i] = x + cost[i+2]
        #    i -= 1
        #
        #if cost[0] < cost[1]:
        #    return cost[0]
        #else:
        #    return cost[1]
        
        
        #def climber(step, cost, price, base_price):
        #    if price >= base_price:
        #        return price
        #    if step >= len(cost):
        #        return price
        #    price += cost[step]
        #    step_1 = climber(step+1, cost, price, base_price)
        #    step_2 = climber(step+2, cost, price, base_price)
        #    if step_1 < step_2:
        #        return step_1
        #    else:
        #        return step_2
        #
        #base_price = 0
        #
        #for x, item in enumerate(cost):
        #    if x%2 == 0:
        #        base_price += cost[x]
        #
        #from_0 = climber(0, cost, 0, base_price)
        #from_1 = climber(1, cost, 0, base_price)
        #
        #if from_0 > from_1:
        #    return from_1
        #else:
        #    return from_0
        
        #price = 0
        #step = 0
        
        #for x, item in enumerate(cost):
        #    print(price, step)
        #    if x != step or x + 1 > len(cost):
        #        continue
        #    if cost[x] < cost[x+1]:
        #        price += cost[x]
        #        step += 1
        #    else:
        #        price += cost[x+1]
        #        step += 2
        #
        #return price
'''
Success
Details 
Runtime: 99 ms, faster than 41.72% of Python3 online submissions for Min Cost Climbing Stairs.
Memory Usage: 13.9 MB, less than 97.18% of Python3 online submissions for Min Cost Climbing Stairs.
'''