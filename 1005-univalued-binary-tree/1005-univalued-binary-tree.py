# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        
        ss = set()

        
        def dfs(node):
            if node == None:
                return 
            
            ss.add(node.val)
            dfs(node.left)
            dfs(node.right)
        

        dfs(root)
        return len(ss) == 1