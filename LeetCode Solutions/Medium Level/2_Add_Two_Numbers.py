'''
2. Add Two Numbers

Medium

20730

4092

Add to List

Share
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        prev = dummy
        tens = 0
        
        while l1 or l2:
            if l1 and l2:
                total = l1.val + l2.val + tens
            elif l1:
                total = l1.val + tens
            elif l2:
                total = l2.val + tens
            ones = total % 10
            tens = total//10
            
            new = ListNode()
            new.val = ones
            if prev:
                prev.next = new
            prev  = new
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            
        if tens > 0:
            new = ListNode()
            new.val = tens
            prev.next = new
        
        return dummy.next

'''
Success
Details 
Runtime: 82 ms, faster than 78.97% of Python3 online submissions for Add Two Numbers.
Memory Usage: 13.9 MB, less than 44.03% of Python3 online submissions for Add Two Numbers.
'''