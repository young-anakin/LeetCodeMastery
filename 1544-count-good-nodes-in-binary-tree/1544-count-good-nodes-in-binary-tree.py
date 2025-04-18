# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cp = 0
        # mx = float("-inf")
        def dfs(node, mx):
            nonlocal cp
            if node == None:
                return
            
            if node.val >= mx:
                mx = node.val
                cp +=1
            
            dfs(node.left, mx)
            dfs(node.right, mx)
        
        dfs(root, float("-inf"))

        return cp