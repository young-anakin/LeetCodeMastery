class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        maxx = -float("inf")
        good = defaultdict(int)

        def check_goodness(node, maxx, good):
            if node == None:
                return
            if maxx <= node.val:
                print("We found gold!")
                good[0] += 1
                maxx = node.val
            check_goodness(node.left, maxx, good)
            check_goodness(node.right, maxx, good)
        
        check_goodness(root, maxx, good)

        return good[0]