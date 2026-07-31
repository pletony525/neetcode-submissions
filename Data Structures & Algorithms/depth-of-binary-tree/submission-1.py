# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(current: Optional[TreeNode], curDepth) -> int:
            if not current:
                return curDepth
            return max(dfs(current.left, curDepth + 1), dfs(current.right, curDepth + 1))

        return dfs(root, 0)

            



        