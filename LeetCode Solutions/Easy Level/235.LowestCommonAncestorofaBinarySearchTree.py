'''
235. Lowest Common Ancestor of a Binary Search Tree

Easy

6473

207

Add to List

Share
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [2,1], p = 2, q = 1
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the BST.

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        cur = root
        
        while cur:
            if cur.val < p.val and cur.val < q.val:
                cur = cur.right
            elif cur.val > p.val and cur.val > q.val:
                cur = cur.left
            else:
                return cur


'''
Success
Details 
Runtime: 165 ms, faster than 11.07% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
Memory Usage: 18.8 MB, less than 68.08% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
'''

# Beginning Structure of Attempt Two

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        cur = root
        if p.val > q.val:
            p, q = q, p
        
        def dfs(root, p, q, cur):
            if root and (root == p or root == q):
                cur = root
                print(cur.val)
                return
            
            elif root and p.val < root.val and q.val > root.val:
                cur = root
                return
            elif root:
                left = dfs(root.left, p, q, cur)
                right = dfs(root.right, p, q)
                return
            else:
                return
        
        dfs(root, p, q)
        
        return cur
    
    '''
    NO SOLUTION
    '''
    
    # Revisited first solution
    
    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        cur = root
        
        while cur:
            if cur.val > p.val and cur.val > q.val:
                cur = cur.left
            elif cur.val < p.val and cur.val < q.val:
                cur = cur.right
            else:
                return cur
            
'''
Success
Details 
Runtime: 114 ms, faster than 58.68% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
Memory Usage: 18.7 MB, less than 68.71% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
'''