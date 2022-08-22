'''
110. Balanced Binary Tree

Easy

6958

362

Add to List

Share
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = [True]
        
        def dfs(root):
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            if abs(left - right) > 1:
                res[0] = False
            
            return 1 + max(left, right)
        
        dfs(root)
        return res[0]


'''
Success
Details 
Runtime: 127 ms, faster than 7.39% of Python3 online submissions for Balanced Binary Tree.
Memory Usage: 18.5 MB, less than 90.57% of Python3 online submissions for Balanced Binary Tree.
'''
#Solution 2

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = [True]
        
        def dfs(root):
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            if res[0] == False:
                return
            if abs(left - right) > 1:
                res[0] = False
            
            return 1 + max(left, right)
        
        dfs(root)
        return res[0]

'''
Success
Details 
Runtime: 104 ms, faster than 22.02% of Python3 online submissions for Balanced Binary Tree.
Memory Usage: 18.6 MB, less than 61.23% of Python3 online submissions for Balanced Binary Tree.
'''
# Neat Code Solution (Faster, Uses more memory)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root: return [True, 0]
            
            left, right = dfs(root.left), dfs(root.right)
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)
            
            return [balanced, 1 + max(left[1], right[1])]
        
        return dfs(root)[0]

'''
Success
Details 
Runtime: 85 ms, faster than 47.91% of Python3 online submissions for Balanced Binary Tree.
Memory Usage: 18.9 MB, less than 30.47% of Python3 online submissions for Balanced Binary Tree.
'''