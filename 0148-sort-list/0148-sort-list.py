# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(left_half,right_half) -> List[int]:
            # write your code here
            
            new = ListNode(0)
            temp = new
            l = 0
            r = 0
            while left_half != None and right_half != None:
                if left_half.val <= right_half.val:
                    temp.next = ListNode(left_half.val)
                    left_half = left_half.next
                else:
                    temp.next =ListNode(right_half.val)
                    right_half = right_half.next
                temp = temp.next
            if left_half:
                temp.next = left_half
            if right_half:
                temp.next = right_half
            new = new.next
            return new
        def mergesort(h, c):

            if not h or not h.next:
                return h

            mid = h

            for _ in range(c//2 - 1):
                mid = mid.next
            
            temp = mid.next
            mid.next = None

            left = mergesort(h, c// 2)
            right = mergesort(temp, ceil(c/2))

            return merge(left, right)


        temp = head
        c = 1

        while temp:
            temp = temp.next
            c += 1

        return mergesort(head, c)