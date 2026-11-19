# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def balance(node):
            if not node:
                return (0, True)
             
            lh, lb = balance(node.left)
            rh, rb = balance(node.right)

            if abs(lh - rh) > 1:
                return (1 + max(lh, rh), False)
            else:
                return (1 + max(lh, rh), lb and rb)

        return balance(root)[1]