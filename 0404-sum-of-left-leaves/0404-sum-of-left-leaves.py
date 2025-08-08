# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        # DFS 

        sm = 0

        # if it's left -> True (check)
        def dfs(node, check):
            nonlocal sm
            if not node:
                return
            
            if check == True and node.left == None and node.right == None:
                sm += node.val
            
            dfs(node.left, True)
            dfs(node.right, False)
        
        dfs(root, False)

        return sm
