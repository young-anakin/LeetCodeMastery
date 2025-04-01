# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dd = defaultdict(list)


        def bfs(root, level, depth):
            if root == None:
                return
            dd[level].append((depth, root.val))
            bfs(root.left, level -1, depth+1)
            bfs(root.right, level + 1, depth+1)
        
        bfs(root, 0, 0)
        ans = []
        for key, val in dd.items():
            ans.append((key, val))  

        ans.sort()    
        fin = []
        # print(ans)
        for val in ans:
            x = sorted(val[1])
            temp = []
            for j in range(len(x)):
                temp.append(x[j][1])
            fin.append(temp)
        # print(dd)
        return fin