'''
278. First Bad Version

Easy

5465

2044

Add to List

Share
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

 

Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
Example 2:

Input: n = 1, bad = 1
Output: 1
 

Constraints:

1 <= bad <= n <= 231 - 1
'''
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        if isBadVersion(1) == True:
            return 1
        last_good = 1
        last_bad = n
        
        while True:
            mid = int(ceil((last_good + last_bad)/2))
            is_bad = isBadVersion(mid)
            if last_bad == (last_good + 1) or last_bad == last_good:
                return last_bad
            elif is_bad == True:
                last_bad = mid
            elif is_bad == False:
                last_good = mid

'''
Success
Details 
Runtime: 57 ms, faster than 20.13% of Python3 online submissions for First Bad Version.
Memory Usage: 14 MB, less than 12.71% of Python3 online submissions for First Bad Version.
'''