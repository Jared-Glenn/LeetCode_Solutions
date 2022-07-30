'''
347. Top K Frequent Elements

Medium

10257

399

Add to List

Share
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''
# Solution 1
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        res = []
        
        for num in nums:
            hmap[num] = 1 + hmap.get(num, 0)
        
        for x in range(k):
            res.append(max(hmap, key=hmap.get))
            del hmap[max(hmap, key=hmap.get)]
        
        return res

'''
Success
Details 
Runtime: 350 ms, faster than 5.02% of Python3 online submissions for Top K Frequent Elements.
Memory Usage: 18.6 MB, less than 91.71% of Python3 online submissions for Top K Frequent Elements.
'''

# Solution 2

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) +1)]
        
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, fre in count.items():
            freq[fre].append(num)
        
        res = []
        for x in range(len(freq) - 1, 0, -1):
            for n in freq[x]:
                res.append(n)
                if len(res) == k:
                    return res

'''
Success
Details 
Runtime: 192 ms, faster than 30.53% of Python3 online submissions for Top K Frequent Elements.
Memory Usage: 19.7 MB, less than 14.94% of Python3 online submissions for Top K Frequent Elements.
'''