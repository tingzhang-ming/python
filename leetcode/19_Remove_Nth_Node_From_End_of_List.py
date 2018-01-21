"""
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.
Try to do this in one pass. 
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return None
        pre, cur, die = head, head, head
        for i in range(n-1):
            pre = pre.next
        if not pre.next:
            return head.next
        while pre.next is not None:
            die = cur
            pre = pre.next
            cur = cur.next
        die.next = cur.next
        return head

    def removeNthFromEnd2(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return None
        l = 0
        p = head
        while p is not None:
            p = p.next
            l += 1
        i = l - n
        if i == 0:
            return head.next
        q = p = head
        for ii in range(i):
            q = p
            p = p.next
        q.next = p.next
        return head
