# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        levels = defaultdict(int)

        def bfs(root, level):
            if root == None:
                return

            
            levels[level] += root.val

            bfs(root.left, level+1)
            bfs(root.right, level+1)
        
        arr = []
        bfs(root, 0)
        for key, val in levels.items():
            arr.append(val)
        
        arr.sort()
        print(arr)
        if k > len(arr):
            return -1
        return arr[-k]