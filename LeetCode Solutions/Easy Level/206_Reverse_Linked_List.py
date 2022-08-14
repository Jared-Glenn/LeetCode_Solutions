'''
206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        first = True
        current = None
        
        while head:
            if first == True:
                current = head
                head = head.next
                current.next = None
                last = current
                first = False
                print("current",current.val,"last",last.val)
            else:
                current = head
                head = head.next
                current.next = last
                last = current
                print("next",current.next.val,"current",current.val,"last",last.val)

            
        return current


'''
Success
Details 
Runtime: 208 ms, faster than 5.14% of Python online submissions for Reverse Linked List.
Memory Usage: 15.5 MB, less than 53.04% of Python online submissions for Reverse Linked List.
'''
# Secod Solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        
        while head:
            nex = head.next
            head.next = prev
            prev = head
            head = nex
        
        return prev

'''
Success
Details 
Runtime: 38 ms, faster than 92.06% of Python3 online submissions for Reverse Linked List.
Memory Usage: 15.4 MB, less than 56.26% of Python3 online submissions for Reverse Linked List.
'''