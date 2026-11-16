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
            
            left_height, left_balance = balance(node.left)
            right_height, right_balance = balance(node.right)
            balanced = left_balance and right_balance
            balanced &= (abs(left_height - right_height) <= 1)

            return (1 + max(left_height, right_height), balanced)        

        return balance(root)[1]