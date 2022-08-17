'''
19. Remove Nth Node From End of List

Medium

11808

523

Add to List

Share
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 

Follow up: Could you do this in one pass?
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head.next
        count = 0
        prev = None
        
        while fast and fast.next:
            count += 1
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        if count == 0 and fast:
            if n == 2:
                return head.next
            else:
                head.next = None
                return head
        elif count == 0:
            return
        
        moves = count - n + 1
        if moves >= 0:
            start = slow
            if fast:
                moves += 1
        else:
            start = head
            moves += count
            if fast:
                moves += 1
            if moves == 0:
                return head.next
        
        while moves > 0:
            moves -= 1
            prev = start
            start = start.next
        
        if start.next:
            prev.next = start.next
        elif prev:
            prev.next = None
            
        return head



'''
Success
Details 
Runtime: 59 ms, faster than 32.48% of Python3 online submissions for Remove Nth Node From End of List.
Memory Usage: 14 MB, less than 20.55% of Python3 online submissions for Remove Nth Node From End of List.
'''