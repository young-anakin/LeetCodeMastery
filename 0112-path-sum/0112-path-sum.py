# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        # DFS Traversal
        # 1. Recursion - Tree 
        # 2. Stack
        if root == None:
            return False
        def dfs(node, sm):
            # Base Case
            # print(node.val)
            if node == None:
                return False
            if node.left == None and node.right == None:
                sm += node.val
                if sm != targetSum:
                    return False
                else:
                    return True

            # Function call
            sm += node.val
            # Left Traversal

            # True or False => True
            return dfs(node.left, sm) or dfs(node.right, sm)
        
            # Right Traversal
            
        
        return dfs(root, 0)
        
