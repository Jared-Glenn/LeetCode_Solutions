'''
104. Maximum Depth of Binary Tree

Easy

8141

137

Add to List

Share
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def countDepth(parent, count):
            if not parent:
                return 0
            count += 1
            this_count = count
            
            if parent.left and parent.right:
                return max(countDepth(parent.left, this_count), countDepth(parent.right, this_count))
            elif parent.left:
                return countDepth(parent.left, this_count)
            elif parent.right:
                return countDepth(parent.right, this_count)
            else:
                return this_count
            

        return countDepth(root, 0)
        

'''
Success
Details 
Runtime: 59 ms, faster than 63.56% of Python3 online submissions for Maximum Depth of Binary Tree.
Memory Usage: 16.2 MB, less than 55.57% of Python3 online submissions for Maximum Depth of Binary Tree.
'''