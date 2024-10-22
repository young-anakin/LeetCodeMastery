# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        dd = defaultdict(int)
        def bfs(node, level):
            if node == None:
                return
            dd[level] += node.val

            bfs(node.left, level+1)
            bfs(node.right, level+1)

        bfs(root, 1)
        mx = -1 * float("inf")
        ans = 0
        for key, val in dd.items():
            if val > mx:
                
                mx = max(val, mx)
                ans = key
        return ans