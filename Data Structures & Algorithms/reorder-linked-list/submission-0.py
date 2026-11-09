# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        result = []
        start = head

        while start:
            result.append(start.val)
            start = start.next

        print(result)
        dummy = ListNode(result[0])
        left = 1
        right = len(result) - 1
        output = dummy
        while left <= right:
            if left == right:
                output.next = ListNode(result[right])
                break
            output.next = ListNode(result[right])
            output.next.next = ListNode(result[left])
            output = output.next.next
            left += 1
            right -= 1
        
        top = dummy
        final = []
        while top:
            final.append(top.val)
            top = top.next
        
        head.next = dummy.next
        print(final)
            


        