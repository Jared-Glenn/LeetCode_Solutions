'''
74. Search a 2D Matrix

Medium

9017

294

Add to List

Share
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix) - 1
        
        while low < high:
            mid = int((low + high)/2)
            if matrix[mid][0] == target:
                return True
            elif low == mid and matrix[mid+1][0] > target:
                break
            elif low == mid and matrix[mid+1][0] <= target:
                low = mid + 1
            elif matrix[mid][0] < target:
                low = mid
            else:
                high = mid - 1
                
        lst = low
        low = 0
        high = len(matrix[lst]) - 1
        
        while low <= high:
            mid = int((low + high)/2)
            if matrix[lst][mid] == target:
                return True
            elif matrix[lst][mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False

'''
Success
Details 
Runtime: 48 ms, faster than 90.53% of Python3 online submissions for Search a 2D Matrix.
Memory Usage: 14.4 MB, less than 42.97% of Python3 online submissions for Search a 2D Matrix.
Next challenges:

'''