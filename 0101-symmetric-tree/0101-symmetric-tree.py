# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        treeOneDict = defaultdict(list)
        treeTwoDict = defaultdict(list)

        if not root:
            return False
        treeOne = root.left
        treeTwo = root.right


        def dfs(node, level, dd):
            if node == None:
                dd[level].append(None)
                return
            
            dd[level].append(node.val)
            dfs(node.left, level+1, dd)
            dfs(node.right, level+1, dd)


        dfs(treeOne, 0, treeOneDict)
        dfs(treeTwo, 0, treeTwoDict)

        for key, val in treeTwoDict.items():
            # Compare the two values 
            otherVal = treeOneDict[key]
            if otherVal[::-1] != val:
                return False
        
        return True

        # print(treeOneDict)
        # print(treeTwoDict)





