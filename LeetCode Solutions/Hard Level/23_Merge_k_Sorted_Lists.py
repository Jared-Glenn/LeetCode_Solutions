'''
23. Merge k Sorted Lists

Hard

13677

522

Add to List

Share
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        res = []
        
        for i, head in enumerate(lists):
            if lists and head == None:
                res.append(i)
        
        while res:
            del lists[res.pop(-1)]
        
        res = None
        
        while lists:
            minimum = float('inf')
            minhead  = None
            ind = 0
            for i, head in enumerate(lists):
                if head:
                    val = head.val
                    if minimum > val:
                        minimum = val
                        minhead = head
                        ind  = i
            if res == None:
                res = minhead
            else:
                prev.next = minhead
            prev = minhead
            if minhead and minhead.next:
                lists[ind] = minhead.next
            else:
                del lists[ind]

        return res

'''
Success
Details 
Runtime: 5293 ms, faster than 5.78% of Python3 online submissions for Merge k Sorted Lists.
Memory Usage: 17.7 MB, less than 61.33% of Python3 online submissions for Merge k Sorted Lists.
'''