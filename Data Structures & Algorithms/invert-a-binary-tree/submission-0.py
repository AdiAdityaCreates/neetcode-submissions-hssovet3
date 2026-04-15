# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def invert(root):
    if root is None:
        return None

    root.left , root.right = root.right , root.left
    invert(root.left)
    invert(root.right)
    return root
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return invert(root)
        