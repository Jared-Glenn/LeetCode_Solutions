'''
25. Reverse Nodes in k-Group

Hard

8639

528

Add to List

Share
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
 

Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000
 

Follow-up: Can you solve the problem in O(1) extra memory space?
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Will return at end
        start_full_loop = None
        
        # The previous beginning, now the end of a loop
        last_in_loop = head
        
        # Storage for previous loop to attach to first of next loop
        last_in_prev_loop = None
        
        # Main Loop
        while head:
            # Counts to ensure we can go the full k distance
            for i in range(k):
                if head:
                    head = head.next
                elif last_in_prev_loop:
                    last_in_prev_loop.next = last_in_loop
                    return start_full_loop
                else:
                    return last_in_loop
            
            # Returns head to the beginning
            head = last_in_loop
            prev = None
            
            # Swap the pointers
            for i in range(k):
                if head.next:
                    nxt = head.next
                else:
                    nxt = None
                head.next = prev
                prev = head
                head = nxt
                
            # Set the start of the full loop
            if start_full_loop == None:
                start_full_loop = prev
            
            if last_in_prev_loop:
                last_in_prev_loop.next = prev
            last_in_prev_loop = last_in_loop
            last_in_loop = head
        
        return start_full_loop
'''
Success
Details 
Runtime: 82 ms, faster than 41.67% of Python3 online submissions for Reverse Nodes in k-Group.
Memory Usage: 15.2 MB, less than 84.35% of Python3 online submissions for Reverse Nodes in k-Group.
'''