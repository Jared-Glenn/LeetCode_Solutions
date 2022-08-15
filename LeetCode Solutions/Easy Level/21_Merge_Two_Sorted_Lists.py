'''
21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]


((Gained additional assistance from a video at: https://www.youtube.com/watch?v=XIdigk956u0&ab_channel=NeetCode ))

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        tail = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
            
        return dummy.next
        
'''
Success
Details 
Runtime: 28 ms, faster than 77.72% of Python online submissions for Merge Two Sorted Lists.
Memory Usage: 13.6 MB, less than 31.73% of Python online submissions for Merge Two Sorted Lists.
Next challenges:
'''

# Solution 2

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 == None and list2 == None:
            return
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        
        if list1.val <= list2.val:
            res = list1
            cur = list1
            placeholder = list2
        else:
            res = list2
            cur = list2
            placeholder = list1
        
        while cur:
            if cur.next or placeholder == None:
                if placeholder == None or cur.next.val < placeholder.val:
                    cur = cur.next
                elif cur.next.val >= placeholder.val:
                    hold = cur.next
                    cur.next = placeholder
                    placeholder = hold
                    cur = cur.next
            elif placeholder:
                cur.next = placeholder
                placeholder = None
            
        return res
    
    '''
    Success
Details 
Runtime: 40 ms, faster than 91.12% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 14 MB, less than 32.66% of Python3 online submissions for Merge Two Sorted Lists.
    '''