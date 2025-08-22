# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        ans = ListNode(10)
        head = ans

        heap = list()

        heapq.heapify(heap)

        for i, el in enumerate(lists):
            if el:
                heapq.heappush(heap, (el.val, i, el))
        
        while heap:
            val, i, el = heapq.heappop(heap)

            curr = ListNode(val)
            head.next = curr
            head = head.next
            el = el.next
            if el:
                heapq.heappush(heap, (el.val, i, el))
        
        return ans.next



