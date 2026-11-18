# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slow is now at the midpoint, reverse the back half
        second_half = slow.next
        slow.next = None

        trav = second_half
        prev = None


        while trav:
            n = trav.next
            trav.next = prev
            prev = trav
            trav = n

        t1 = head
        t2 = prev

        while t1 and t2:
            n1 = t1.next
            n2 = t2.next

            t1.next = t2
            t1 = n1
            t2.next = t1
            t2 = n2
            

