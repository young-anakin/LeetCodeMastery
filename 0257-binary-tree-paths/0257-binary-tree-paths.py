# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        ans = []
        def traverse(node, val):
            if not node:
                return
            if not node.left and not node.right:
                val.append(str(node.val))
                ans.append("->".join(val))
                return
            val.append(str(node.val))
            traverse(node.left, val[:] )
            traverse(node.right, val[:] )

        
        traverse(root, [])
        return (ans)