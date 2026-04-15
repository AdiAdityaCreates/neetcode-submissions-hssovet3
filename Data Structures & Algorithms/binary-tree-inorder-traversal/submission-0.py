# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def inoorder(root,res):
    if root is None:
        return []

    inoorder(root.left,res)
    res.append(root.val)
    inoorder(root.right,res)
    return res
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        return inoorder(root,res)
        