# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        newHead = None
        prev = None
        node = head
        while node is not None and node.next is not None:
            if node.next.val == node.val:
                while node.next and node.next.val == node.val:
                    node.next = node.next.next
                if prev:
                    prev.next = node.next    
            else:
                prev = node
                if newHead is None:
                    newHead = prev
            node = node.next
        if (not newHead) and node:
            return node
        return newHead