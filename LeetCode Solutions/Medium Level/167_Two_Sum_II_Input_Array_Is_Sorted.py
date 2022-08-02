'''
167. Two Sum II - Input Array Is Sorted

Medium

7132

1038

Add to List

Share
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
 

Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.
'''
# Solution 1

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = 0
        high = 1
        max = len(numbers) - 1
        
        while True:
            if high > max:
                low +=1
                high = low+1
            elif numbers[low] == numbers[high] and (numbers[low] + numbers[high]) != target:
                low = high
                high += 1
            elif (numbers[low] + numbers[high]) == target:
                return [(low+1), (high+1)]
            elif (numbers[low] + numbers[high]) < target:
                high += 1
            else:
                low +=1
                high = low+1



'''
Success
Details 
Runtime: 259 ms, faster than 17.95% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
Memory Usage: 14.9 MB, less than 41.40% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
'''


# Solution 2

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = 0
        high = len(numbers) - 1
        
        while True:
            if (numbers[low] + numbers[high]) == target:
                return [(low+1), (high+1)]
            elif (numbers[low] + numbers[high]) < target:
                low += 1
            else:
                high -= 1

'''
Success
Details 
Runtime: 210 ms, faster than 46.56% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
Memory Usage: 15 MB, less than 41.40% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
'''