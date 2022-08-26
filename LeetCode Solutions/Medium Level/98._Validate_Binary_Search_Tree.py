'''
98. Validate Binary Search Tree

Medium

10798

932

Add to List

Share
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
'''
'''
Old Version: (This one only checks the previous node, not each previous node.)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        list_of_nodes = [root]
        
        valid_BST = True
        
        while valid_BST == True and len(list_of_nodes) > 0:
            root = list_of_nodes.pop(0)

            try:
                if root.left.val >= root.val:
                    valid_BST = False
                    print("BST FALSE, root:", root.val, "left:", root.left.val)
                    continue
                else:
                    list_of_nodes.append(root.left)
            except:
                print("LEFT--NO--","list:", len(list_of_nodes))
                pass
            try:
                if root.right.val <= root.val:
                    valid_BST = False
                    print("BST FALSE, root:", root.val, "right:", root.right.val)
                    continue
                else:
                    list_of_nodes.append(root.right)
            except:
                ("RIGHT--NO--", len(list_of_nodes))
                pass
            print('length:', len(list_of_nodes), list_of_nodes)
            
        
        return valid_BST

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(node, left, right):
            if not node:
                return True
            if not (node.val > left and node.val < right):
                return False
            
            return (valid(node.left, left, node.val)) and (valid(node.right, node.val, right))
        
        return(valid(root, float('-inf'), float('inf')))


'''
Success
Details 
Runtime: 43 ms, faster than 96.42% of Python3 online submissions for Validate Binary Search Tree.
Memory Usage: 16.4 MB, less than 78.61% of Python3 online submissions for Validate Binary Search Tree.
'''

# Solution 2

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
            
        def checking(root, minimum, maximum):
            if not root: return True
            
            left = checking(root.left, minimum, root.val)
            right = checking(root.right, root.val, maximum)
            
            valid = (left and right and root.val < maximum and root.val > minimum)
            
            return valid
        
        return checking(root, float('-inf'), float('inf'))

'''
Success
Details 
Runtime: 78 ms, faster than 35.80% of Python3 online submissions for Validate Binary Search Tree.
Memory Usage: 17.1 MB, less than 5.40% of Python3 online submissions for Validate Binary Search Tree.
'''