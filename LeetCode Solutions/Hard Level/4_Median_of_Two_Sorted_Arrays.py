'''
4. Median of Two Sorted Arrays

Hard

18680

2169

Add to List

Share
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) +  len(B)
        half = total//2
        
        # A needs to be shorter
        if len(A) > len(B):
            A, B = B, A
        
        l, r = 0, len(A) - 1
        while True:
            i = (l+r)//2
            j = half - i - 2
            
            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i+1] if (i+1) < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j+1] if (j+1) < len(B) else float("inf")
            
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return ((max(Aleft, Bleft))+(min(Aright, Bright)))/2
            elif Aright < Bleft:
                l = i + 1
            else:
                r = i - 1
                


'''
Success
Details 
Runtime: 186 ms, faster than 20.33% of Python3 online submissions for Median of Two Sorted Arrays.
Memory Usage: 14.2 MB, less than 25.87% of Python3 online submissions for Median of Two Sorted Arrays.
'''