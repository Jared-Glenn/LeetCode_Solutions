'''
105. Construct Binary Tree from Preorder and Inorder Traversal

Medium

10710

289

Add to List

Share
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
 

Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
'''

# Previous Code - Not very elegant.

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
#         #while preorder:
#         value = preorder[0]
#         del preorder[0]
#         new = TreeNode()
#         new.val = value
#         if inorder.index(value) > 0:
#             left = TreeNode()
#             new.left = left
#             new.left.val = preorder[0]
        
#         print(new.val, new.left.val)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left  = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root

'''
Success
Details 
Runtime: 410 ms, faster than 11.13% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
Memory Usage: 88.6 MB, less than 22.22% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
'''