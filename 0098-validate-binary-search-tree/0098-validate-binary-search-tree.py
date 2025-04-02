# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def bfs(node, lowerBound, upperBound):
            if node == None:
                return True
            
            if node.val <= lowerBound or node.val >= upperBound:
                return False
            
            
            # let's traverse to the left

            a =  bfs(node.left, lowerBound, node.val)

            # let's traverse to the right

            b =  bfs(node.right, node.val, upperBound)

            return (a and b)
        
        return bfs(root, float("-inf"), float("inf"))
        
