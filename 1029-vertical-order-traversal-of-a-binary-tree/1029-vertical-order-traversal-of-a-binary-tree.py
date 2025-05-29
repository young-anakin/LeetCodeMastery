# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = defaultdict(list)

        def dfs(node, level, height):
            if node == None:
                return
            
            levels[level].append((height, node.val))
            dfs(node.left, level -1, height+1)
            dfs(node.right, level +1, height + 1)
        
        ans = []

        dfs(root, 0, 0)
        # print(levels)
        sorted_levels = dict(sorted(levels.items()))
        for key, val in sorted_levels.items():
            val.sort()
            tmp = []
            for idx in val:
                tmp.append(idx[1])
            ans.append(tmp)
        
        return ans
