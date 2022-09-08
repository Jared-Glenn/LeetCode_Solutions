'''
40. Combination Sum II

Medium

6772

167

Add to List

Share
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
'''

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        
        subset = []
        def backtracking(i, add):
            if add > target:
                return
            if add == target:
                if subset not in res:
                    res.append(subset.copy())
                return
            if i >= len(candidates):
                return
            
            subset.append(candidates[i])
            backtracking(i+1, add + candidates[i])
            
            subset.pop()
            j = i
            while j < len(candidates) and candidates[j] == candidates [i]:
                j +=1
            backtracking(j, add)
        
        backtracking(0, 0)
        return res

'''
Success
Details 
Runtime: 238 ms, faster than 8.03% of Python3 online submissions for Combination Sum II.
Memory Usage: 13.8 MB, less than 93.29% of Python3 online submissions for Combination Sum II.
'''