'''
589. N-ary Tree Preorder Traversal

Easy

2003

96

Add to List

Share
Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

 

Example 1:



Input: root = [1,null,3,2,4,null,5,6]
Output: [1,3,5,6,2,4]
Example 2:



Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
0 <= Node.val <= 104
The height of the n-ary tree is less than or equal to 1000.
 

Follow up: Recursive solution is trivial, could you do it iteratively?

'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        output_list = []
        children_list = [root]
        new_children = []
        
        while len(children_list) > 0:
            root = children_list.pop(0)
            try:
                output_list.append(root.val)
                if root.children:
                    new_children.extend(root.children)
                    while len(new_children) > 0:
                        child = new_children.pop(-1)
                        children_list.insert(0, child)
            except:
                pass
        
        return output_list


'''
Success
Details 
Runtime: 72 ms, faster than 62.29% of Python3 online submissions for N-ary Tree Preorder Traversal.
Memory Usage: 16 MB, less than 80.40% of Python3 online submissions for N-ary Tree Preorder Traversal.
'''