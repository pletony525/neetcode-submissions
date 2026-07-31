# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #1 + dfs(node.left, pathlen) + dfs(node.right, pathlen)
        res = 0
        def dfs(currentNode) -> int:
            nonlocal res
            if not currentNode:
                return 0
            
            leftpath = dfs(currentNode.left)
            rightpath = dfs(currentNode.right)
            res = max(res, leftpath  + rightpath)
            return 1 + max(leftpath, rightpath)
        dfs(root)
        return res

            
