# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        levels = defaultdict(lambda: float('-inf'))
        if root == None:
            return []
        def dfs(node, level):
            if node == None:
                return
            
            levels[level] = max(node.val, levels[level])
            dfs(node.left, level+1)
            dfs(node.right, level+1)
        
        dfs(root, 0)
        ans = []
        for key, val in levels.items():
            ans.append(val)
        
        return ans


