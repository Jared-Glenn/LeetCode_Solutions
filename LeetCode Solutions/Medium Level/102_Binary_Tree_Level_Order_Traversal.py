'''
102. Binary Tree Level Order Traversal

Medium

9701

190

Add to List

Share
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output_list = []
        root_list = [root]
        children_list = []
        holding_list = []
        going = True
        
        while going == True:
            for r in root_list:
                try:
                    holding_list.append(r.val)
                except:
                    pass
                try:
                    children_list.append(r.left)
                except:
                    continue
                try:
                    children_list.append(r.right)
                except:
                    pass
            root_list = []
            if len(holding_list) == 0:
                going = False
                pass
            else:
                output_list.append(holding_list)
                holding_list = []
                root_list.extend(children_list)
                children_list = []
            
        return output_list

'''
Success
Details 
Runtime: 59 ms, faster than 37.38% of Python3 online submissions for Binary Tree Level Order Traversal.
Memory Usage: 14.1 MB, less than 98.89% of Python3 online submissions for Binary Tree Level Order Traversal.
'''

# Second Solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()
        q.append(root)
        
        while q:
            level = []
            qLen = len(q)
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        
        return res

'''
Success
Details 
Runtime: 43 ms, faster than 78.62% of Python3 online submissions for Binary Tree Level Order Traversal.
Memory Usage: 14.2 MB, less than 85.22% of Python3 online submissions for Binary Tree Level Order Traversal.
'''