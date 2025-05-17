# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        sm = 0
        dd = defaultdict(int)
        def dp(node, parent, grandparent):
            if not node:
                return
            nonlocal sm
            if grandparent:
                sm += node.val
            if node.val % 2 == 0:
                print(node.val)
                dp(node.left, True, parent)
                dp(node.right, True, parent)

            elif node.val % 2 == 1:
                dp(node.left, False, parent)
                dp(node.right, False, parent)

        
        dp(root, False, False)
        return sm