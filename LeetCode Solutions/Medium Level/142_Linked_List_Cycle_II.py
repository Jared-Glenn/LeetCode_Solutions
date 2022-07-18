'''
142. Linked List Cycle II

Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
Example 2:


Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.
Example 3:


Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
 

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        lst = []
        

        while head:
            if head in lst:
                return head
            lst.append(head)
            head = head.next
        return None

'''
Success
Details 
Runtime: 986 ms, faster than 6.31% of Python3 online submissions for Linked List Cycle II.
Memory Usage: 17.3 MB, less than 94.27% of Python3 online submissions for Linked List Cycle II.



SOLUTION 2
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        
        slow, fast = head, head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        
        if not fast.next or not fast.next.next:
            return
        
        slow2 = head
        
        while slow.next:
            if slow == slow2:
                return slow
            slow = slow.next
            slow2 = slow2.next  
        
        return
    
    '''
    Success
Details 
Runtime: 87 ms, faster than 38.91% of Python3 online submissions for Linked List Cycle II.
Memory Usage: 17.4 MB, less than 31.53% of Python3 online submissions for Linked List Cycle II.
    '''