# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        dd = defaultdict(int)

        def dfs(root):
            if root == None:
                return 0

            

            x = dfs(root.right)
            y = dfs(root.left)

            dd[root.val + x + y] +=1 

            return root.val + x + y


        dfs(root)

        x = max(dd.values())
        ans = []
        for key, val in dd.items():
            if val == x:
                ans.append(key)

        # print(dd)

        return ans