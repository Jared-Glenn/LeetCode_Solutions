'''
572. Subtree of Another Tree

Easy

6032

328

Add to List

Share
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 

Example 1:


Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
Example 2:


Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
 

Constraints:

The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-104 <= root.val <= 104
-104 <= subRoot.val <= 104
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs2(root, subRoot):
            if not root and not subRoot:
                return True
            elif not root or not subRoot:
                return False
            
            left, right = dfs2(root.left, subRoot.left), dfs2(root.right, subRoot.right)
            same = (left and right and root.val == subRoot.val)
            
            return same
        
        
        def dfs(root, subRoot):
            if not root: return False
            
            if root.val == subRoot.val and dfs2(root, subRoot) == True:
                return True
            else:
                left, right = dfs(root.left, subRoot), dfs(root.right, subRoot)
                sub = (left or right)
                
                return sub
        
        return dfs(root, subRoot)

'''
Success
Details 
Runtime: 219 ms, faster than 32.16% of Python3 online submissions for Subtree of Another Tree.
Memory Usage: 15.1 MB, less than 35.97% of Python3 online submissions for Subtree of Another Tree.
'''