'''
739. Daily Temperatures

Medium

7787

172

Add to List

Share
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
'''
# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         stack = []
#         output = []
#         count = 1
        
#         for num in temperatures:
#             output.append(0)
            
#             while stack and num > stack[-1]:
#                 stack.pop()
#                 count += 1
#                 print('first while:', stack, count)
            
#             for i in range(count):
#                 output.pop()
#                 print(output)
                
#             while count > 0:
#                 output.append(count)
#                 count -= 1
        
#             stack.append(num)
        
#         return output

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)
        
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackT, stackInd = stack.pop()
                output[stackInd] = i - stackInd

            stack.append([temp, i])
        
        return output


'''
Success
Details 
Runtime: 1718 ms, faster than 58.94% of Python3 online submissions for Daily Temperatures.
Memory Usage: 24.7 MB, less than 70.83% of Python3 online submissions for Daily Temperatures.

'''