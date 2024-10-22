# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        l, r = 0, 0
        fl = True
        def traverse(node, d):
            nonlocal fl
            if node == None:
                return d
            

            x = traverse(node.left, d+1)
            y = traverse(node.right, d+1)
            # print(x, y)
            if abs(x-y) > 1:
                fl = False

            return max(x, y)

        traverse(root, 0)
        
        return fl