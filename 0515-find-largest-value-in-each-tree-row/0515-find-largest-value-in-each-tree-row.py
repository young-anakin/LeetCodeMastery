# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

        elements = defaultdict(list)

        # level 0 - [1]
        # Level 1 - [3, 2]
        # Level 2 - [5, 3 , 9]


        # Parameter
        # Base case
        # Logic 

        def dfs(level, node):
            # Base Case
            if node == None:
                return
            
            elements[level].append(node.val)

            dfs(level+1, node.left)
            dfs(level+1, node.right)


        dfs(0, root)
        ans = []

        for key, val in elements.items():
            ans.append(max(val))
        
        return ans


                


