# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        cp = 0
        def dfs(node):

            nonlocal cp
            if not node:
                return []
            
            if not node.left and not node.right:
                return [1]
            
            a = dfs(node.left)
            b = dfs(node.right)

            for x in a:
                for y in b:
                    if x + y <= distance:
                        cp +=1
            
            z = a + b

            return [1 + i for i in z]
        dfs(root)
        return cp
