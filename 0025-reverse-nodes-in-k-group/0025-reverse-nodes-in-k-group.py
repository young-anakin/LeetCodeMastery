# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node = ListNode(9)
        cp = 0

        tmp = head
        while tmp:
            tmp = tmp.next
            cp +=1
        
        print(cp)
        tmp = head
        # print(tmp)
        bucket = []
        ans = node
        x = 0
        for ind in range(cp):
            # print("ans", tmp.val)
            bucket.append(tmp.val)
            x +=1
            tmp = tmp.next
            if x == k:
                bucket = bucket[::-1]
                # print(bucket)
                for j in bucket:
                    ll = ListNode(j)
                    ans.next = ll
                    ans = ans.next
                
                bucket = []
                x = 0
        for j in bucket:
            ll = ListNode(j)
            ans.next = ll
            ans = ans.next       
        node = node.next
        return node