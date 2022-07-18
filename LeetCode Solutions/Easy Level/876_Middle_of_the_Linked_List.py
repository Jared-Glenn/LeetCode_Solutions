'''
876. Middle of the Linked List

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:


Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 

Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100

'''

import math

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        original = head
        
        count = 0
        
        while head:
            count += 1
            head = head.next
        
        middle = (math.floor(count/2) + 1)
        
        if count == 1:
            return original
        
        iterations = 1
        
        while iterations < middle:
            iterations += 1
            original = original.next
            
        return original
    
    '''
    Success
Details 
Runtime: 47 ms, faster than 51.57% of Python3 online submissions for Middle of the Linked List.
Memory Usage: 13.9 MB, less than 55.26% of Python3 online submissions for Middle of the Linked List.
    
    '''