# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # splitting list
        
        second = slow.next
        slow.next = None

        # flip the second half

        prev = None

        while second:
            after = second.next
            second.next = prev
            prev = second
            second = after

        #merge & alternate

        first = head
        second = prev

        while second:
            firstafter = first.next
            secondafter = second.next

            first.next = second
            second.next = firstafter

            first = firstafter
            second = secondafter
        








            



