# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    res = 0
    
    def goodNodes(self, root: TreeNode) -> int:


        def dfs(node, upper):
            if not node:
                return
            
            if node.val >= upper:
                self.res += 1
            
            dfs(node.left, max(node.val, upper))
            dfs(node.right, max(node.val, upper))


        dfs(root, -float('inf'))
        return self.res 


        