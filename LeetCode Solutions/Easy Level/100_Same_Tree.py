'''
100. Same Tree

Easy

6816

149

Add to List

Share
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false
 

Constraints:

The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs2(p_root, q_root):
            if not p_root and not q_root: return [True]
            elif not p_root or not q_root: return [False]
            
            left, right = dfs2(p_root.left, q_root.left), dfs2(p_root.right, q_root.right)
            same = (left[0] and right[0] and p_root.val == q_root.val)
            
            return [same]
        
        return dfs2(p, q)[0]

'''
Success
Details 
Runtime: 56 ms, faster than 26.64% of Python3 online submissions for Same Tree.
Memory Usage: 13.9 MB, less than 76.30% of Python3 online submissions for Same Tree.
'''